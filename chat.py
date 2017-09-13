# -*- encoding: utf-8 -*-

import asyncore
import socket

class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind((host, port))
        self.buffer = ''

    def handle_read(self):
        self.buffer, self.addr = self.recvfrom(20)
        print self.buffer
    def writable(self):
        return (len(self.buffer) > 2)
    def handle_write(self):
        sent = self.sendto(self.buffer, self.addr)
        self.buffer = self.buffer[sent:]

server = EchoServer('localhost', 8080)
asyncore.loop()