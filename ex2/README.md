# TCP File Server

## Overview

This project involves implementing a TCP server that allows clients to request and download files. The server expects the client to send the name of the file it wishes to download. The files are stored in a folder named "files," located in the same directory as the server.

## File Request Format

The client sends a request to the server in the following format:

GET [file] HTTP/1.1

If the file name is a single slash ("/"), it is interpreted as requesting the file named "index.html."

Additional lines in the message are ignored by the server. The client signals the end of the message by sending a newline character twice (`\r\n\r\n`).

## Server Response

If the file exists, the server responds with:

HTTP/1.1 200 OK
Connection: [conn]
Content-Length: [length]

Followed by a blank line and the contents of the file.

- `[conn]`: Value of the Connection field from the client's request.
- `[length]`: Size of the sent file in bytes.

For example:

HTTP/1.1 200 OK
Connection: close
Content-Length: 11

Hello world

If the value of the Connection field is "close," the server closes the connection after sending the file. If it is "keep-alive," the server keeps the connection open for the client's next file request.

## Handling Timeouts

To handle potential timeouts, the server sets a maximum time period for the socket stuck on `recv` using a timeout. If the server does not receive a response after 1 second or receives empty requests from the client, it closes the current connection and handles the next client (new connection).

## Binary Files (jpg or ico)

For files with extensions "jpg" or "ico," the server reads the content in binary form and sends it in the response.

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: [length]
[binary image data]

## File Not Found

If the file does not exist, the server responds with:

HTTP/1.1 404 Not Found
Connection: close

## Redirect

If the client requests a file named "/redirect," the server responds with:

HTTP/1.1 301 Moved Permanently
Connection: close
Location: /result.html

Be sure to return an empty line after the "Location" line in the response.

## Logging

The server prints the requests received from the client to the screen.

## Server Usage

Run the server with the following command:

python server.py [port]
For example:

python server.py 8080
Access the server using your browser by entering the following in the address bar:

http://[Server IP]:[Server port][Path]

For example:

http://1.2.3.4:8080/
Replace [Server IP] and [Server port] with the server's IP address and port. [Path] is the path to the file as defined above.

Note: In this exercise, you are not writing a client; you will use an existing client, such as your browser (Chrome), to interact with the server.

