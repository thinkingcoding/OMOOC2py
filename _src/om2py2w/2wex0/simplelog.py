# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
simplelog GUI for windows8.1
author: wwshen
2015-11-3
'''

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8') #解决输入中文出错的问题

from Tkinter import *
import tkFont

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
content = txt.read()

class application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.create_Widgets()
	
	#从控件读取输入并删除	
	def rtrv_input(self, event):
		more = event.widget.get(1.0, "end")
		event.widget.delete(1.0, "end")
		txt = open('simplelog.txt', 'r+')
		global content
		content = content + more
		txt.write(content)
		self.readonly.config(state = 'normal')
		self.readonly.insert('end', more)
		
	def create_Widgets(self):
		#字体
		T16 = tkFont.Font(family="Times", size = 16)
		T12 = tkFont.Font(family="Times", size = 12)
		
		#文本显示窗口
		self.readonly= Text(self, autoseparators = True, 
			bg = 'gray90', font = T12, height = 25, width = 80)
		self.scrl0 = Scrollbar(self, command = self.readonly.yview)
		self.scrl0.grid(row=0, column=1, sticky = NS)
		self.readonly.config(yscrollcommand=self.scrl0.set)
		self.readonly.insert('end', content)
		self.readonly.config(state='disabled')
		self.readonly.grid(row=0, column=0,sticky=EW)
		
		#输入框窗口
		self.newtext = Text(self, bg = 'white', font = T16, height = 5, width = 60)
		self.scrl1 = Scrollbar(self, command = self.newtext.yview)
		self.scrl1.grid(row=1,column=1, sticky =NS)
		self.newtext.config(yscrollcommand=self.scrl1.set)
		self.newtext.bind('<Return>', self.rtrv_input)
		self.newtext.grid(row=1, column=0, sticky=EW)
		
		#quit按钮
		self.enter = Button(self, text = 'quit', command = self.quit)
		self.enter.grid(row=2,column=0,columnspan=2, sticky=EW)
		

	
app = application() # create the application
app.master.title('SimpleLog') #name appears at the top
app.mainloop()		#start the program

# record the input into the file


# save
txt.close()
