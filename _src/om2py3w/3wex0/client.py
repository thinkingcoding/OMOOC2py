# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket

HOST = '192.168.1.114'
PORT = 50007
ADDRESS = (HOST, PORT)
bufsize = 1024

print 'waiting for connection...'
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(ADDRESS)
#connection,address = s.accept()
print '...connected from', ADDRESS

while True:
	content = cs.recv(bufsize)
	print content
	if content =='end of the log':
		break

print 'type q() to quit inputting'		
while True:
	#客户和服务器通过send和recv方法通信。
	line = raw_input('>:')
	cs.send(line)
	if line == 'q()':
		break

#结束后，客户通过调用socket的close方法来关闭连接
cs.close()
