#!/bin/python
import socket
recv_ip="13.232.121.204"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((recv_ip, recv_port))
while(true):
	data= s.recvfrom(100)
	print(data)

#To reply to sender 
s.sendto("ok got it",data[1])




