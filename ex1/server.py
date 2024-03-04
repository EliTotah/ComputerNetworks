import socket
import sys

# Function to save addresses to a file
def save_adresses(file_name, map1):
    try:
        with open(file_name, 'w') as file:
            for web_add,ip_add in map1.items():
                file.write(f"{web_add},{ip_add}\n")
    except Exception as e:
        print(f"Error: {e} ")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("num of args incorrect")
        sys.exit(1)
        
    # Parse command-line arguments
    my_port = int(sys.argv[1])
    parent_ip = sys.argv[2]
    parent_port = int(sys.argv[3])
    ips_file_name = sys.argv[4]

    # Create a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Dictionary to store mappings of web addresses to IP addresses    
    ip_map = {}

    try: 
        # Read existing mappings from the file
        with open(ips_file_name,'r') as file:
            
            for line in file:
                web_address, ip_address = map(str.strip, line.split(','))
                ip_map[web_address] = ip_address

        # Bind the socket to the specified port
            s.bind(('', my_port))

        # Continuously listen for incoming messages
            while True:

            # Receive data and client address from the socket
                data, client_address = s.recvfrom(1024)
                web_address = data.decode()

            # Check if the web address is in the mappings
                if web_address in ip_map:
                    ip_address = ip_map[web_address]
                    s.sendto(ip_address.encode(), client_address)

                else:
            # Check if we are in the parent server
                    if (parent_ip == "-1" and parent_port == -1):
                        s.sendto(b"Adress does not exist",client_address)
                
                    else :
            # we are in the son server
            # Forward the request to the parent server
                        s.sendto(data,(parent_ip,parent_port))
                        data1,parent_address = s.recvfrom(1024)
                # Check if we got ip in the parent server's response
                        if (data1.decode() != "Adress does not exist"):
                            ip_map[web_address] = data1.decode()
                # Save the updated mappings to the file
                            save_adresses(ips_file_name,ip_map)
                        s.sendto(data1,client_address)

    except FileNotFoundError:
        print(f"the file was not fount")
    except Exception as e:
        print(f"Error: {e} ")
