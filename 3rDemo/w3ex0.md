####python：联机CLI版的极简日志制作
- 要求：在上周开发基础上, 完成 极简交互式笔记的网络版本
- 需求如下:
- 每次运行时合理的打印出过往的所有笔记
  - 一次接收输入一行笔记
  - 在服务端保存为文件:
  - 在所有访问的客户端可以获得历史笔记
  - 支持多个客户端同时进行笔记记录

- 知识储备
  - python - [socket](https://docs.python.org/2.7/library/socket.html)
  - TCP与UDP连接
  - 关于socket的几个中文教程
    - [python 网络编程学习: 1 初识 SOCKET](http://www.cnblogs.com/cacique/archive/2012/08/05/2623995.html)
	- [python socket编程详细介绍](http://yangrong.blog.51cto.com/6945369/1339593)
	
######编写
- beta3.0
  - 注：初始版本，属于审题不合格的作品。
  - 存在问题：
    - 使用TCP连接
	- 不支持多客户端同时访问。
	
  - 这一作品基本上照抄中文教程。
  - 需要分别编写服务器端和客户端程序。
    - 服务器端主要负责发送历史笔记、接收客户端数据、写入并保存文件
    - 客户端主要接收历史笔记、使用raw_input进行输入并传递给客户端。
    - 使用时分别打开服务器端和客户端的程序。根据服务器端的ip不同，客户端的HOST需要重新手动写入。
- sever端程序	
		# -*- coding: utf-8 -*-
		#!/usr/bin/env python

		import socket
		import os
		from time import ctime

		#全局变量
		global txt, New_ctnt

		HOST = '' #''表示连接到任意可用地址
		PORT = 50007 #随意数字
		ADDRESS = (HOST, PORT)
		bufsize = 1024 #接收的最大数据量
		fn = 'simplelog.txt' #记录日志的文件
		New_ctnt = '' #新纪录
		
		#（创建并）打开日志记录文件，读取内容
		FileExist = os.path.exists('simplelog.txt')
		if FileExist:
			txt = open(fn, 'r+')
		else:
			txt = open(fn,'w') 
			txt = open(fn, 'r+')
		content = txt.read()
		
		#建立连接s
		#建立一个socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#使用bind公开一个端口，方便client连接
		s.bind(ADDRESS)
		#设置一个listen队列的大小。
		s.listen(1)

		try:
			while True: #与客户端建立连接
				print 'waiting for connection ...'
				#服务器套接字通过socket的accept方法等待客户请求一个链接：
				connection,address = s.accept()
				print '...connected from', address
				break
			
			while True: #发送数据（历史日志）
				tr_cntnt = content[0:(bufsize-1)]
				print tr_cntnt
				connection.send(tr_cntnt)
				if len(content) <= bufsize:
					print 'end of the log'
					connection.send('end of the log')
					break
				else:
					content = content[bufsize: -1]
	
			while True: #接收数据（新写入日志）
				line = connection.recv(bufsize)
				if line == 'q()':
					break
				New_ctnt = New_ctnt + '\n' + line
				print line

		except BaseException, e:			
			connection.close()

		#写入文件	
		txt.read()	
		txt.write(New_ctnt)
		txt.close()

- client程序
		# -*- coding: utf-8 -*-
		#!/usr/bin/env python

		import socket

		HOST = '192.168.1.114' #为服务器端的ipv6
		PORT = 50007 #为服务器端指定的端口
		ADDRESS = (HOST, PORT)
		bufsize = 1024

		print 'waiting for connection...'
		cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		cs.connect(ADDRESS)
		print '...connected from', ADDRESS

		while True: #接收服务器端的数据（历史日志）
			content = cs.recv(bufsize)
			print content
			if content =='end of the log':
				break

		print 'type q() to quit inputting'		
		while True: #发送数据（新日志）
			#客户和服务器通过send和recv方法通信。
			line = raw_input('>:')
			cs.send(line)
			if line == 'q()':
				break

		#结束后，客户通过调用socket的close方法来关闭连接
		cs.close()