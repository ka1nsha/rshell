#-*- coding:utf-8 -*-
import socket
from thread import *
host = "127.0.0.1"
port = 8080
buff = 2048
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
binding = host,port
client_socket.bind(binding)
client_socket.listen(10)
def sendcode(c,ac):
    c.send(ac)
    data = c.recv(2048)
    if not data:
        pass
    if data == "PAR0LA":
        parola = raw_input("Enter Password : \n")
        parola = parola.decode("utf-8")
        sendcode(c,parola)
    else:
        print data
c,addr = client_socket.accept()
while True:

    ac = raw_input(" > \n")
    ac.decode("utf-8")
    sendcode(c,ac)

# if __name__ == '__main__':
#     t = Thread(target=req(),name="t1")
#
# e.start()