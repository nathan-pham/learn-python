import socket

handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Enter a url: ")
host = url.split('/').pop(0)

handle.connect((host, 80))

body = f"GET http://{url} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode()

handle.send(body)

while True:
	data = handle.recv(512)
	if len(data) < 1:
		break
	print(data.decode())

handle.close()