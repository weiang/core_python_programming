#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from socket import * 

HOST = 'localhost'
PORT = 22222
ADDR = (HOST, PORT)
BUFSIZ = 1024

clnt_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    clnt_socket.sendto(data, ADDR)
    data, ADDR = clnt_socket.recvfrom(BUFSIZ)
    print '%s' % data

clnt_socket.close()
