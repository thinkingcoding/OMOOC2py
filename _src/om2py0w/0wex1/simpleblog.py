# -*- coding: utf-8 -*-
# 一个极简交互式日记系统，作用如下：
# 一次接收输入一行日记
# 保存为本地文件
# 再次运行系统时，打印出过往的所有日记


import os
global txt, index 
WDir = os.getcwd()
fn = 'simpleblog.txt'

# determine if the file has existed.
index = 0
for root, dirs, files in os.walk(WDir):
	for name in files:
		if name == fn:
			index = index + 1
		else:
			index = index + 0

#Print the file, or create a file
if index == 0:
	txt = open(fn, 'w')
	txt = open(fn, 'r+')
else:
	txt = open(fn, 'r+')
	print txt.read()
			
# enter from the user
more = raw_input ( "Enter: ")

# reading the newline and add into the old
ori = txt.read()
txt.write(ori)
txt.write('\n')
txt.write(more)

# save
txt.close()