#####极简日志<Simplelog>人机交互版制作日志
- 操作系统：windows8.1

- 此版本为Week2的作业，要求使用Tkinter作为GUI的工具制作“极简日志”
- 学习Tkinter是一个全新的过程，我大概花了3-4天的时间才大概读懂几个documentation，然后学会搭框架。
- 在人机交互界面下，程序出错的可能增加，debug的难度增大，中途崩溃，休息了两三天。
- 随后参考了同学作业如
  - [bambooom](https://github.com/bambooom/OMOOC2py/blob/master/_src/om2py2w/2wex0/diarygui.py)
  - [wzzlj](https://github.com/wzzlj/OMOOC2py/blob/master/_src/om2py2w/2wex0/daily.py)
  - 两个同学均为Mac的系统
  
  
- 几个槛
  - 对于Tkinter的基本理解
    - 基本框架，采用以下方式编写框架
			class Application(Frame):
				def __init__(self, master=None) #设计主面吧
				self.grid() #使主面板出现，grid为使用格子方式布局控件
				self.creat_widgets() #所有控件，见下
				
				def creat_widgets(self):
					self.text1 = Text(self) #文本框1
					self.tex1.grid() #在主面板上布局文本框1
					self.text2 = Text(self) #文本框2
					self.text2.grid() #布局文本框2
				
			app = Application() # create the application
			app.master.title('SimpleLog') #name appears at the top
			app.mainloop()	#运行
    - grid是布局空间的万能形式，它使用格子形式布局。从左到右分别为column0，1，2……，从上到下分别为row0，1，2，……。每一个控件占一个格子，不分大小。因此只要将控件在纸上布局好，就可以按照它们的位置编号，并运行grid()
	- event：发生事件（如击回车）导致控件改变。我的问题是没有找到在“一个控件单击回车，使另一个控件打印文本”的方法。后来参照bambooom的编译，发现我function写错了地方。我写在class外面，改成写在class内部后不再出错。
  - write()出错（文件打开方式为'r+'
    - 错误为error 0
    - 以 python write() error 0 为关键词，发现[stackflow](http://stackoverflow.com/questions/19881890/ioerror-errno-0-error-in-python)里有人遭遇了类似的错误。
    - 查看讨论，发现有人提到read和write语句一起出现时会出现报错，原因不详。于是尝试把read的语句往上提，在程序最初出现，并赋值给一个变量，问题解决。	
    - 比较三个版本：
      - 版本1（CLI,more为单次输入语句）：
					ori = txt.read()
					txt.write(ori)
					txt.write('\n')
					txt.write(more)
      - 版本2（CLI，content为程序结束前所有新增语句）					
					txt.read()
					txt.write(content)
      - 版本3（GUI，content为文档原有内容+所有新增语句）
					txt = open('simplelog.txt', 'r+')
					global content            #| content = txt.read() 
					content = content + more 
					txt.write(content)
      - 1/2都是read write一起出现，无报错。3(当为#后语句)则报错。
      - 1/3 read后，write是从第一行开始的（覆盖原文件），而2却是继文件尾续写。
	  - 不知何故。需要进一步观察。  
  - GUI界面输入中文报错
    - 直接参考了两位同学的语句。
			import sys
			reload(sys)
			sys.setdefaultencoding('utf8')
  - 另版本2中将语句中的True改为1也会出错
			while True:
				more = raw_input('>:')
				if more == "q()":
					break
				else:
				content += '\n'+ more
    - 没有出错提示，但会漏掉输入的句子：输入两句，漏掉一句。需要进一步观察。			