import socket

handle = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url = input("Enter a url: ")
host = url.split('/').pop(0)

handle.connect((host, 80))

body = f"GET http://{url} HTTP/1.1\r\nHost: {host}\r\n\r\n".encode()

handle.send(body)

main_loop = True

while main_loop:
    data = handle.recv(512)
    decoded = data.decode()
    if len(data) < 1:
        main_loop = False
    
    for line in decoded.split('\r\n'):
        if line == '':
            main_loop = False
            break
            
        print(line)

handle.close()