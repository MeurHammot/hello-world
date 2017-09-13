# -*- encoding: utf-8 -*-

import socket

UDP_IP = "172.16.17.140"
UDP_PORT = 5060
MESSAGE = "INVITE"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(20) # buffer size is 1024 bytes
print "received message:", data