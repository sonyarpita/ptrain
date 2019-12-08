import socket
def client_program():
	host="192.168.0.97" #socket.gethostname() #as bot code is running on same machine 
	port=5000 #socket server port number 
	client_socket=socket.socket() #instantiate
	client_socket.connect((host,port)) # connect function takes tuple as argument hence (())
	message=input("-> ") #take input
	while message.lower().strip() != "bye":
		client_socket.send(message.encode())#send message 
		data =client_socket.recv(1024).decode() #recieve response
		print("Recieved from server: " + data) #show in terminal
		message=input("-> ") #again take input 
	client_socket.close() #close connection
client_program()
