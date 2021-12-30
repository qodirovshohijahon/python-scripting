import socket

host_name = socket.gethostname()
port = 3000
s_socket = socket.socket()
s_socket.bind((host_name, port))
s_socket.listen(2)

con, address = s_socket.accept()
print("Connection from: " + str(address))

while True:
    data = con.recv(1024).decode()
    if not data:
        break
    print("from connected user:" + str(data))
    data = input(" -> ")
    con.send(data.encode())