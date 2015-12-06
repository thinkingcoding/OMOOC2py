# -*- coding: utf-8 -*-
#qpy:main.py

#qpy:webapp:StoryChain
#qpy:fullscreen
#qpy://localhost:8080
"""
以上代码运行时将会用 WebView 以全屏模式打开 localhost:8080
"""
from bottle import template, request, response, redirect, HTTPResponse
from bottle import Bottle, ServerAdapter
from bottle import debug

import sqlite3

from os import path
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#import androidhelper
#Droid = androidhelper.Android()

#数据库
stories = 'storychain.db'
users = 'users.db'

#开启调试
debug(True)

#创建数据库
if not path.exists(stories):
	import createstorydata
if not path.exists(users):
	import createuserdata

root = path.dirname(path.abspath(__file__))	
	
#/newuser /index: 判断重名
def checkdup(list, value):
	check = False
	for i in list:
		print i
		i = reduce(i,i)
		if i == value:
			check = True
			break
	return check

#/login: 检查用户名和密码
def check_login(u,p):
	c = 0
	up = (u, p)
	userdata = sqlite3.connect(users)
	uc = userdata.cursor()
	check = False
	while True:
		uc.execute("SELECT count(count) FROM users")
		maxcount = reduce(x, uc.fetchone())
		uc.execute("SELECT userid, password FROM users WHERE count=?", (c,))
		ups = uc.fetchone()
		if c > maxcount:
			userdata.commit()
			break
		elif ups == up:
			check = True
			userdata.commit()
		else:
			c += 1
	return check

class MyWSGIRefServer(ServerAdapter):
	server = None
	def run(self, handler):
		from wsgiref.simple_server import make_server, WSGIRequestHandler
		if self.quiet:
			class QuietHandler(WSGIRequestHandler):
				def log_request(*args, **kw): pass
			self.options['handler_class'] = QuietHandler
		self.server = make_server(self.host, self.port, handler, **self.options)
		self.server.serve_forever()

	def stop(self):
		#sys.stderr.close()
		import threading
		threading.Thread(target=self.server.shutdown).start()
		#self.server.shutdown()
		self.server.server_close() #<--- alternative but causes bad fd exception
		print "# qpyhttpd stop"

def __exit():
	global server
	server.stop()

def __ping():
	return 'ok'

def index():
	user = request.get_cookie('account', secret='somekey')
	conn = sqlite3.connect(stories)
	cc=conn.cursor()
	cc.execute("SELECT title, main FROM chains WHERE count=?", (0,))
	ALL = cc.fetchall()
	conn.commit()
	temallstory = root+'/allstory')
	output = template(temallstory, userid = user, rows = ALL, information='')
	if request.GET.get('save'):
		user = request.get_cookie('account',secret='somekey')
		if not users:
			output = template(temallstory, userid=user, rows = ALL, information='请登录')
		else:
			newtitle = unicode(request.GET.get('title'))
			conn = sqlite3.connect(stories)
			cc = conn.cursor()
			cc.execute("SELECT title FROM chains")
			AllTitle = cc.fetchall()
			conn.commit()	
			if checkdup(AllTitle, newtitle):
				output = template(temallstory, userid=user, rows = ALL, information='重名，请重新输入')
				return output
			else:
				newurl='/'+newtitle
				redirect (newurl)
	if request.GET.get('exit'):
		__exit()
	return output

def body(name):
	conn = sqlite3.connect(stories)
	cc = conn.cursor()
	t = unicode(name)
	tembody = root+'/body.tpl'
	if request.GET.get('save'):
		user = request.get_cookie('account',secret='somekey')
		if not user:
			output = template(tembody, rows = result, title=name, information='请先登录！')
		else:	
			new = unicode(request.GET.get('main'))
			currentT = datetime.now()
			ShowT = currentT.strftime('%Y-%m-%d %H:%M:%S')
			cc.execute("SELECT title FROM chains")
			AllTitle = cc.fetchall()
			count = 0
			if checkdup(AllTitle, t):
				cc.execute("SELECT count(count) FROM chains WHERE title=?", (t,))
				x=cc.fetchone()
				count =reduce(x, x)
			cc.execute("INSERT INTO chains VALUES(?,?,?,?,?)", (t, count, new,user,ShowT))
			conn.commit()
	cc.execute("SELECT * FROM chains WHERE title=? ORDER BY count", (t,))
	result = cc.fetchall()
	output = template(temallstory, rows = result, title=name,information='')
	return output	

def login():
	return template(root+'/login', information='')

def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if check_login(username, password):
		response.set_cookie('account',username, secret='somekey')
		redirect('/index')
	else:
		return template(root+'/login', information='登录失败，请确认用户名和密码，或注册新账号')

def newuser(information=''):
	return template(root+'/reg',information='')

def do_newuser():
	username = request.forms.get('username')
	password = request.forms.get('password')
	confirm = request.forms.get('confirm')
	userdata = sqlite3.connect(users)
	uc = userdata.cursor()
	uc.execute("SELECT userid FROM users")
	alluser = uc.fetchall()
	if checkdup(alluser, username):
		return template(root+'/reg', information='该用户名已存在！')
	elif password == confirm:
		uc.execute("SELECT count(count) FROM users")
		x = uc.fetchone()
		Newcount = reduce(x, x)
		uc.execute("INSERT INTO users VALUES(?,?,?)",
			(Newcount, username, password))
		userdata.commit()	
		redirect('/login') 
	else:
		return template(root+'/reg', information='请确保两次输入的密码相同！')		
	
#MyWSGIRefSever
if __name__ == '__main__':
	app = Bottle()
	app.route('/')(index)
	app.route('/index', method='GET')(index)
	app.route('/:name', method='GET')(body)
	app.route('/login', method= 'GET')(login)
	app.route('/login', method= 'POST')(do_login)
	app.route('/newuser', method = 'GET')(newuser)
	app.route('/newuser', method = 'POST')(do_newuser)
	app.route('/__exit', method=['GET','HEAD'])(__exit) #自我结束功能
	app.route('/__ping', method=['GET','HEAD'])(__ping) #健康监测

	try:
		server = MyWSGIRefServer(host="localhost", port="8080")
		app.run(server=server,reloader=True)
	except Exception,ex:
		print "Exception: %s" % repr(ex)
	
