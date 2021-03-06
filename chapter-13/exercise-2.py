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
    decoded = data.decode()
    
    if length < 1:
    	break

    for char in decoded:
        total_length += 1
        if total_length < 3000:
            print(char, end='')

print(total_length)
handle.close()