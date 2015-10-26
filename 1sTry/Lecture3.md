######比较水的感触
- **触动1** 睡觉
  - Keep calm and go sleep
  - 作为一个后进生，咱天天鼓励自己不耻于后，勇敢前进。听完一堂课，有太多的梗要挖，但还是先睡觉……
- **触动2** 框架
  - 写w0ex1的时候，虽然有意识搭好框架，但随意性还是蛮大的，八股框架显然更值得借鉴。另外我发现自己居然有好多函数没用到。需要在写w0ex1教程（以及update）时补一下
- **触动3** 
  - 全部操作用CLI好酷炫。不过我估计自己用windows还有好多年。
  - 给自己用CLI，给别人用GUI（念鬼吧），聪明人都这么干……
  - The Zen of Python 需要细挖。
  - 芝麻星要好好看完，我只看了101交互是不对的……
   
---

######1w4d Lecture3 (or 2)
主讲：大妈 时间：2015-10-22
- 0w表扬
  - wp-lai的编程效率
  - ajiea的诗意（课程整体体验）
  - zoe的教程（第二人称）
- 程序员的CLI日常
  - **文章**
    - 终端之威
    - [完全用命令行工作](http://blog.youxw.info/categoy/keyboard/)
    - 完全用Linux工作，摒弃windows（王垠）
- REPL的探索
  - (复制粘贴)“读取-求值-输出”循环（英语：Read-Eval-Print Loop，简称REPL）是一个简单的，交互式的编程环境。这个词常常用于指代一个Lisp的交互式开发环境，但也能指代命令行的模式和例如APL、BASIC、Clojure、F#、Haskell、J、Julia、Perl、PHP、Prolog、Python、R、Ruby、Scala、Smalltalk、Standard ML、Tcl、Javascript这样的编程语言所拥有的类似的编程环境。这也被称做交互式顶层构件（interactive toplevel）。
  - keep calm and try dir()/help()/ipython
  - PyENV
- 如何完成1w任务
  - ** .pyc?**
    - 是由py文件经过编译后生成的二进制文件
  - 技术
    - raw_input() 从外界输入
	- **while + break** 保持交互 + 退出
	- **os.path.exists** 本地文件是否存在这个状态的获得
	- **?!?!?**
	- open()
	- **for .. in**
	  - **粗体**的是我在极简日志作业中未曾用到的function
- UTF-8字符集的故事
  - ASCII 128个字符
  - Unicode 包含1, 000, 000+字符: 但是浪费空间
  - UTF-8变长的编码，最通用
  - GB2312（定长） -GB13000 -GBK/CP936（定长）-GB18030
  - 中文版windows：CP936
  - 简而言之，utf-8 shell/保存/输出/...以免出问题  
- 善用搜索，受益无穷
- **框架**
    	# -*- coding: utf-8 -*-
	    #!usr/bin/env python
	    # 头部声明
	    '''文件说明
	    作者信息
	    版本自述
	        ...
	    '''
	    #全局引用
	    #全局变量
	    #函数撰写区
	    #自检区
  - "#!usr/bin/env python"是什么，见[[1](http://stackoverflow.com/questions/2429511/why-do-people-write-usr-bin-env-python-on-the-first-line-of-a-python-script)][[2](http://blog.csdn.net/wh_19910525/article/details/8040494)]		
  - **pythonic... The Zen of python  八荣八耻...**
		Beautiful is better than ugly.
		Explicit is better than implicit.
		Simple is better than complex.
		Complex is better than complicated.
		Flat is better than nested.
		Spase is better than dense.
		Readability counts.
		Special cases aren't special enough to break the rules.
		Although practicality beats purity.
		Errors should never pass silently.
		Unless explicitly silenced.
		In the face of ambiguity, refuse the temptation to guess.
		There should be one -- and peferably only one -- obvious way to do it.
		Althoughh that way may not be obvious at first unless you're Dutch.
		Now is better than never.
		Although never is often better than *right* now.
		If the implementation is hard to explain, it's a bad idea.
		If the implementation is easy to explain, it may be a good idea.
		Namespaces are one honking great idea -- lt's do more of those!
    - http://blog.csdn.net/gzlaiyonghao/article/details/2151918		
		 
- 2w任务
  - 引入了GUI
    - 桌面应用Tkinter 见[[1](https://wiki.python.org/moin/TkInter)] [[2](https://docs.python.org/2/library/tkinter.html)]
	  - Tk 小 & 工业-实时控制 http://www.tcl.tk/software/tcltk/
	- check芝麻星
- ps
  - win党
    - 配好路径...
	- **use SSH for github**    
	- **[putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/)（自由软件）** putty.org (国内的注毒)
	  - A Free Telnet/SSH Client
	  - PuTTY是一个Telnet、SSH、rlogin、纯TCP以及串行接口连接软件。较早的版本仅支持Windows平台，在最近的版本中开始支持各类Unix平台，并打算移植至Mac OS X上。除了官方版本外，有许多第三方的团体或个人将PuTTY移植到其他平台上，像是以Symbian为基础的移动电话。
	  - [中文教程](http://chaifeng.com/blog/2007/06/putty_200611.html)