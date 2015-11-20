# -*- coding: utf-8 -*-
#!/usr/bin/env python
#中文输入报错的解决：http://blog.csdn.net/matrix_laboratory/article/details/19163615

from bottle import route, run, redirect, template, request, response, static_file
from bottle import debug
import sqlite3
from os import path
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
fn = 'storychain.db'
users = 'users.db'
debug(True)

#创建数据库
if not path.exists(fn):
	import createstorydata	
if not path.exists(users):
	import createuserdata
	
#/newuser:判断注册重名
def checkdup(list, value):
	check = False
	for x in list:
		x = reduce(x,x)
		if x == value:
			check = True
			break
		else:	
			check= False
	return check	

#/login: 判断用户名和密码是否与数据库中的相同
def check_login(u, p):
	c = 0
	up = (u, p)
	userdata = sqlite3.connect(users)
	uc = userdata.cursor()
	check = False
	while True:
		uc.execute("SELECT count(count) FROM users")
		x = uc.fetchone()
		maxcount = reduce(x,x)
		uc.execute("SELECT userid, password FROM users WHERE count=?", (c,))
		ct = uc.fetchone()
		if c > maxcount:
			check = False
			userdata.commit()
			break
		elif ct == up:
			check = True
			userdata.commit()
			break
		else:
			check = False
			c += 1
	return check

#/storychain: 判断标题是否重名
def check_title(T):
	check = False
	t= (T,)
	conn = sqlite3.connect(fn)
	cc = conn.cursor()
	cc.execute("SELECT title FROM chains")
	AT = cc.fetchall()
	conn.commit()
	for i in AT:
		if i==t:
			check = True
			break
		else:
			check = False
	return check			
	
#用户注册界面
@route('/newuser')
def newuser(information=''):
	return template('reg',information='')

@route('/newuser', method = 'POST')
def do_newuser():
	username = request.forms.get('username')
	password = request.forms.get('password')
	confirm = request.forms.get('confirm')
	userdata = sqlite3.connect(users)
	uc = userdata.cursor()
	uc.execute("SELECT userid FROM users")
	alluser = uc.fetchall()
	if checkdup(alluser, username):
		return template('reg', information='该用户名已存在！')
	elif password == confirm:
		uc.execute("SELECT count(count) FROM users")
		count = uc.fetchone()
		Newcount = reduce(count, count)
		Newcount += 1
		uc.execute("INSERT INTO users VALUES(?,?,?)",
			(Newcount, username, password))
		userdata.commit()	
		redirect('/login') 
	else:
		return template('reg', information='请确保两次输入的密码相同！')

#用户登录界面
@route('')
@route('/')
@route('/login')
def login():
	return template('login', information='')

@route('/login', method = 'POST')
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if check_login(username, password):
		response.set_cookie('account',username, secret='somekey')
		redirect('/storychain')
	else:
		return template('login', information='登录失败，请确认用户名和密码，或注册新账号')

#所有标题显示/添加界面
@route('/storychain', method='get')
def allstory(user='游客'):
	user = request.get_cookie('account', secret='somekey')
	conn = sqlite3.connect(fn)
	cc=conn.cursor()
	cc.execute("SELECT title, main FROM chains WHERE ct=?", (0,))
	ALL = cc.fetchall()
	conn.commit()
	output = template('allstory', userid=user, rows = ALL, information='')
	if request.GET.get('save'):
		newtitle = unicode(request.GET.get('title'))
		if check_title(newtitle):
			output = template('allstory', userid=user, rows = ALL, information='重名，请重新输入')
			return output
		else:
			newurl='/storychain/'+newtitle
			redirect (newurl)
	return output



#单个文档显示/输入界面
@route('/storychain/<name>', method='GET')
def body(name):
	conn = sqlite3.connect(fn)
	cc = conn.cursor()
	t = (unicode(name),)
	if request.GET.get('save'):
		new = unicode(request.GET.get('main'))
		currentT = datetime.now()
		ShowT = currentT.strftime('%Y-%m-%d %H:%M:%S')
		user = request.get_cookie('account',secret='somekey')
		if not check_title(unicode(name)):
			New_ct = 0
		else:
			cc.execute("SELECT ct FROM chains WHERE title=?", t)
			ct = cc.fetchall()
			print ct
			ct = max(ct)
			New_ct = reduce(ct,ct)
			New_ct += 1
		cc.execute("INSERT INTO chains VALUES(?,?,?,?,?)", (unicode(name), New_ct, new,user,ShowT))
		conn.commit()
	cc.execute("SELECT * FROM chains WHERE title=? ORDER BY ct", t)
	result = cc.fetchall()
	output = template('make_table', rows = result, title=name)
	return output
	

#CSS, images
@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root = '/path')
		
run(host='localhost', port=8080, reloader = True)