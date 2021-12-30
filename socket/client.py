import socket

host_name = socket.gethostname()
port = 3000

c_socket = socket.socket()
c_socket.connect((host_name, port))
msg = input(" -> ")

while msg.lower().strip() != 'bye':
    c_socket.send(msg.encode())
    data = c_socket.recv(1024).decode()
    print('Received from server: ' + str(data))
    msg = input(" -> ")
    
c_socket.close()