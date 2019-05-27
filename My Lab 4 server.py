import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
message = "Поступившего ранее сообщения не было"

while True:
    data = conn.recv(2056)
    if not data:
        break
    if data.decode('utf-8') == "Disable Server":
        conn.close()
    conn.send(message.encode('utf-8'))
    message = data.decode('utf-8')


