import socket
import threading
import time

class Server(object):
    '''Server class'''
    connections = {}
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket()
    def start(self):
        self.socket.bind(('', self.port))
        self.socket.listen(1)
        while True:
            conn, addr = self.socket.accept()
            print addr
            Server.connections[addr[0]] = conn
            ct = threading.Thread(target = self.connection, args=(conn,))
            ct.daemon = True
            ct.start()
    def stop(self):
        self.socket.close()
    def connection(self, conn):
        while conn:
            data = conn.recv(1024)
            print data
            if not data:
                break
            conn.send("Got it " + str(data))
        conn.close()
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
        print Server.connections
    elif choise == '0':
        break
    else:
        print 'Wrong choise'