#!/usr/bin/python2

import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    data = 'init'
    while data:
        data = conn.recv(1024)
        if data:
            print 'Received:',data
    print 'Connection lost'
    conn.close()
print 'Exiting.'
