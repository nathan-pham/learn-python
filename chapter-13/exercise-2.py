"""
Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
"""

import socket

handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Enter a url: ")
host = url.split('/').pop(0)

handle.connect((host, 80))

body = f"GET http://{url} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode()

handle.send(body)

total_length = 0
while True:
    data = handle.recv(512)
    length = len(data)
    total_length += length
    if(length < 1):
    	break
    if total_length < 3000:
        print(data.decode())

handle.close()