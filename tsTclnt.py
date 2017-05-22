#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from socket import *

SERV_HOST = 'localhost'
SERV_PORT = 21567
BUFSIZ = 1024
SERV_ADDR = (SERV_HOST, SERV_PORT)

serv_sock = socket(AF_INET, SOCK_STREAM)
serv_sock.connect(SERV_ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    serv_sock.send(data)
    data = serv_sock.recv(BUFSIZ)
    if not data:
        break
    print data

serv_sock.close()
