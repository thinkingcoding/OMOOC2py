# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''文件说明
一个极简交互式日记系统，作用如下：
一次接收输入一行日记
保存为本地文件
再次运行系统时，打印出过往的所有日记
作者：wwshen
时间：2015-10-28
版本：beta1.1   修订每次打开程序只能输入一行日志的问题。
'''

#全局引用
import os

#全局变量
global txt, content

# filename for the records to go to.
fn = 'simplelog.txt' 

# determine if the file has existed.
FileExist = os.path.exists('simplelog.txt')

#Print the file, or create a file
if FileExist:
	txt = open(fn, 'r+')
else:
	# create a file with no reading access
	txt = open(fn,'w') 
	# open the file with read and write access
	txt = open(fn, 'r+')
#read from the simplelog.txt
print txt.read(),'\n'				

# collect input from user
print 'Have fun typing! Type "q()"  to quit!\n'
content =''
while True:
	more = raw_input('>:')
	if more == "q()":
		break
	else:
		content += '\n'+ more
content += '\n'		
print "\nThis is what you have input:"
print content

# record the input into the file
txt.read()
txt.write(content)

# save
txt.close()