#!/bin/python
import socket
recv_ip="172.17.0.2"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(true):
	msg= raw_input("Please enter your message : " )
	s.sendto(msg, (recv_ip,recv_port))
	print(s.recvfrom(10))
