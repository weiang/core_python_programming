#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 22222
ADDR = (HOST, PORT)
BUFSIZ = 1024

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(ADDR)

while True:
    print 'Waiting for message'
    data, client = udp_socket.recvfrom(BUFSIZ)
    print 'Recv data:%s from %s' % (data, client)
    new_data = "[%s] %s" % (ctime(), data)
    udp_socket.sendto(new_data, client)

udp_socket.close()
