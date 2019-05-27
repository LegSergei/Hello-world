import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    mess = input("Введите сообщение\n")
    if mess == "Disable Client":
        break
    sock.send(mess.encode('utf-8'))
    data = sock.recv(2056)
    print(data.decode('utf-8'))

sock.close()