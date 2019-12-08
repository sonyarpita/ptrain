import socket
def server_program():
	#get the hostname
	host="192.168.0.97" #socket.gethostname()
	port= 5000 #initialize port no above 1024 
	server_socket=socket.socket()#create the socket 
	#look close. The bind() function takes tuple as argument 
	server_socket.bind((host,port))#bind host address and port together

	#configure how many cient the server can listem simultaneously 
	server_socket.listen(2)
	conn, address = server_socket.accept()#accept new connection 
	print("Connection from:" + str(address))
	while True:
	# recieve data stream. it wont accept data acet greater tan 1024 bytes 
		data = conn.recv(1024).decode()
		if not data:
			#if data is not recieved break 
			break
		print("from connected user:" + str(data))
		data=input("-> ")
		conn.send(data.encode())#send data to the client
	conn.close() #close the connection
server_program()
