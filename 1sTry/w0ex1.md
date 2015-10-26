- 作业要求
  - 一个极简交互式日记系统，作用如下：
  - 一次接收输入一行日记
  - 保存为本地文件
  - 再次运行系统时，打印出过往的所有日记
  
- 构思
	确定文档是否已经存在
	-->
	如存在 --> 打印出过往所有记录
	如不存在 --> 本地创建新文档
	-->
	给出用户输入窗口
	-->读取用户输入，并加入原记录
	-->保存
- 实现构思需要解决的一些问题
  1. 如何确定文档是否存在？search 并 match 用户的本地文件？
  2. 如何读取文件内容？
  3. 如何创建新文档？
  4. 如何给出用户输入窗口？
  5. 如何读取用户输入内容？
  6. 如何加入原记录？
  7. 如何保存
- 很不幸，对于我来说，每一步都是问题。

- 尝试
  0. 建立架构, 并凭自己的直觉，输入一些命令（参考[LPTHW](http://learnpythonthehardway.org/book/)）
	    	# -*- coding: utf-8 -*-
	    	# 一个极简交互式日记系统，作用如下：
	    	# 一次接收输入一行日记
	    	# 保存为本地文件
	    	# 再次运行系统时，打印出过往的所有日记

		    # determine if the file has existed.

    		#Print the file, or create a file

	    	# enter from the user

		    # reading the newline and add into the old

		    # save
  1. 如何确定文档是否存在？
    - google: use python find/search file (in a directory)
	- 根据google的结果在官方文档查找相关的function，如os，os.path，fnmatch等等
	- 官方文档看不太懂——没关系，可以试错。
	- 结合google搜索到的提示，打出相应的语句。
	- 最初语句如下：
		import os
		WDir = os.getcwd()
		fn = 'simpleblog.txt'
		for root, dirs, files in os.walk(WDir):
		for name in files:
			if name == fn:
				txt = open(fn, 'r+')
				print txt.read()
			else:
				txt = open(fn, 'w')
				txt = open(fn, 'r+')
	- 几次运行发现问题：程序似乎不走if下的语句，直接给出的是else下的结果。
	- 尝试把if和else内的内容改成print 't'和print 'f'，发现问题：for in os.walk将所有文件从上到下查看了一遍，因为最后一个文件的名字并不是我所搜索的文件，而我总是对相同的文件进行操作，因此最后一步操作给出的是文件名不匹配时的操作结果。
	- 因为目标文件数目非1即0，因此改用数数的方法来确定是否存在。
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
  2. 如何读取文件内容？
    - 根据LPTHW，用open语句，查看官方文档open的参数说明，看不懂——就试错
  3. 如何创建新文档？
    - google: how to create a file use python等等，最后发现open语句也能解决这个问题……
  4. 如何读取用户输入内容？
    - 参考LPTHW，用raw.input('')即可
  5. 如何加入原记录？
    - 这里我遇到的问题是对open的不同参数的调用，如'w' 'r' 'r+' 'w+'等
    - 在可读取，可写入状态下用.write依次写入原内容、换行符(\n)、和用户输入内容。这种方式的不足是创建的文件第一行是空行。
  6. 如何保存
    - 参考LPTHW，用.save即可
  7. 其他
    - 过程中会创建一个对象（object），指向目标文档，它的print不同于平时有赋值的函数的一些打印命令。
    - 缩进和“：”等细节不对会导致出错。	