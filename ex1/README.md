
# 144 Digital Service Server

## Overview

This project implements a digital 144 service using the UDP protocol. The goal is to build a server that can receive questions in the form of web addresses and return their corresponding IP addresses. The server loads a mapping file named `txt.ips` before starting, which contains mappings between web addresses and IP addresses.

## Server Functionality

### Mappings File Format

The `txt.ips` file contains mappings in the format: `web_address, IP_address`.

Example:
biu.ac.il, 1.2.3.4
google.co.il, 1.2.3.5

### Handling Queries

The server expects messages containing web addresses and responds with the appropriate IP addresses. If the server doesn't know the IP associated with a web address, it redirects the query to its "father" server. The IP address of the parent server is passed as a parameter to the program. The server redirects the question to the parent server, receives the answer, "learns" it, and answers the customer.

The meaning of "learning" is that from now on, customers asking the server the same question will immediately receive the answer because the server already knows it. The server does not need to ask the server again.

Every time the server learns a new mapping, it saves all the mappings it knows to a `txt.ips` file. The new mappings learned will also be saved to a file. Thus, if the server is closed and restarted, it retains all the "memory" it had last time, including the new things it learned.

## Server and Client Usage

### Server

The server receives four arguments as input to the program:

[myPort] [parentIP] [parentPort] [ipsFileName]

Example of running a parent server:

server.py 55555 -1 -1 parent.txt

Example of running a normal server:

server.py 12345 127.0.0.1 55555 ips.txt

# Client
The client receives two arguments as input to the program:

[serverIP] [serverPort]

Example of running a client:

client.py 127.0.0.1 12345

