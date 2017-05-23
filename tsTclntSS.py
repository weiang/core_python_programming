#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZ = 1024

while True:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        sock.close()
        break
    sock.send('%s\r\n' % data)
    new_data = sock.recv(BUFSIZ)
    print new_data.strip()
    sock.close()

