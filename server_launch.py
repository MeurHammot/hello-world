# -*- encoding: utf-8 -*-

from server import Server
import socket
import threading
import time

srv = Server(1488)
while True:
    print '''
    Enter number for action:
    1. Start
    2. Stop
    3. Connections list
    0. Exit
    '''
    choise = raw_input('> ')
    if choise == '1':
        ct = threading.Thread(target = srv.start)
        ct.daemon = True
        ct.start()
        print 'started'
    elif choise == '2':
        srv.stop()
    elif choise == '3':
        for conn in Server.connections:
            print str(Server.connections[conn][0]),\
            str(Server.connections[conn][1])
    elif choise == '0':
        break
    else:
        print 'Wrong choise'