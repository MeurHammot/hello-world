# -*- encoding: utf-8 -*-

import socket
import threading
import time

class Server(object):
    '''TCP Server class'''
    connections = {}
    threads = {}
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket()
    def start(self):
        self.socket.bind(('', self.port))
        self.socket.listen(1)
        while True:
            conn, addr = self.socket.accept()
            print addr
            Server.connections[conn] = addr
            Server.threads[conn] = threading.Thread(
                target = self.connection, args=(conn,))
            Server.threads[conn].start()
    def stop(self):
        self.socket.close()
    def connection(self, conn):
        while True:
            try:
                data = conn.recv(1024)
                print data
            except Exception as e:
                print 'Client ' + Server.connections[conn][0],\
                str(Server.connections[conn][1]) + ' disconnected!'
                break
            if not data:
                break
            conn.send("Got it " + str(data))
        conn.close()
        del Server.connections[conn]
        del Server.threads[conn]