# -*- encoding: utf-8 -*-

import socket
import time

sock = socket.socket()
sock.connect(('localhost', 1488))
sock.send('Hi there!')
data = sock.recv(1024)
while True:
    print 'ping'
    sock.send('Hi there!')
    kek = raw_input('> ')
    if kek == '0':
        break
sock.close()

