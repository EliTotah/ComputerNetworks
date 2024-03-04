import socket
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("num of args incorrect")
    sys.exit(1)

# Retrieve server IP and port from command-line arguments
server_ip = sys.argv[1]
server_port = int(sys.argv[2])

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Continuously prompt the user for input
while True:
    # get user input
    user_input = input()
    # Send user input to the server
    s.sendto(user_input.encode(), (server_ip, server_port))
    # Receive data from the server
    data, server_adress = s.recvfrom(1024)
    # Print the received data after decoding it from bytes to string
    print(str(data.decode()))