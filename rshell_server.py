#-*- coding:utf-8 -*-
import socket
from thread import *
host = "127.0.0.1"
port = 8080
buff = 2048
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
def req(conn):
    data = conn.recv(2048)
    if not data:
        pass
    else:
        print "Çıktı :" + data.decode("utf-8")

def sendcmd(komut,addr):
    cmd  = raw_input("Code : ")
    cmd = cmd.encode("utf-8")
    client_socket.sendto(komut,addr)
    client_socket.close()
bcp= host,port
client_socket.bind(bcp)
client_socket.listen(10)
data,addr = client_socket.accept()

start_new_thread(req,(data,))
while True:
    print "Connection with " + addr[0] + ":" + str(addr[1])
    komut = raw_input(" > ")



    if komut == "1":
        sendcmd(komut,addr)


# if __name__ == '__main__':
#     t = Thread(target=req(),name="t1")
#
# e.start()