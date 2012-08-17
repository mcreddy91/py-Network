#!/usr/bin/python
import socket
ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	port = int(raw_input("Enter port number to listen: "))
except:
	print "Invalid port..."
	exit()
print "Server listening at port %d..."%port
ser_socket.bind(('',port))
ser_socket.listen(5)
while 1:
	con,client = ser_socket.accept()
	file_name = con.recv(1024)
	if not file_name:
		continue
	f = open(file_name,'w')
	while 1:
		data = con.recv(1024)
		if not data: break
		f.write(data)
	print "Recivied file %s from remote client... saved!"%file_name
	con.close()
