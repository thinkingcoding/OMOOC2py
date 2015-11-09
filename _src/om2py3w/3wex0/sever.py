# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket
import os
from time import ctime

#全局变量
global txt, New_ctnt

HOST = ''
PORT = 50007
ADDRESS = (HOST, PORT)
bufsize = 1024
fn = 'simplelog.txt' 
New_ctnt = ''

FileExist = os.path.exists('simplelog.txt')
if FileExist:
	txt = open(fn, 'r+')
else:
	txt = open(fn,'w') 
	txt = open(fn, 'r+')
content = txt.read()

#建立一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#使用bind公开一个端口，方便client连接
s.bind(ADDRESS)
#设置一个listen队列的大小。
s.listen(1)

try:
	while True:
		print 'waiting for connection ...'
		#服务器套接字通过socket的accept方法等待客户请求一个链接：
		connection,address = s.accept()
		print '...connected from', address
		break
	
	while True:
		tr_cntnt = content[0:(bufsize-1)]
		print tr_cntnt
		connection.send(tr_cntnt)
		if len(content) <= bufsize:
			print 'end of the log'
			connection.send('end of the log')
			break
		else:
			content = content[bufsize: -1]
	
	while True:
		line = connection.recv(bufsize)
		if line == 'q()':
			break
		New_ctnt = New_ctnt + '\n' + line
		print line

except BaseException, e:			
	connection.close()

txt.read()	
txt.write(New_ctnt)
txt.close()