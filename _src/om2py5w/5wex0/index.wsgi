# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sae
import sae.kvdb

from bottle import Bottle
from bottle import run, redirect, template, request, response, static_file
from bottle import debug

from pprint import pprint

from os import path
from datetime import datetime, time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

debug(True)
app = Bottle()

#/newuser:判断重名
def checkdup(anystr):
	check = False
	kv = sae.kvdb.Client()
	key_list = [i for i in kv.getkeys_by_prefix(anystr)]
	if key_list:
		#print key_list
		key_stored = reduce(key_list, key_list)
		if anystr == key_stored:
			check = True
		elif anystr == key_stored[0:-14]:
			check = True
		#print key_stored[0:-14]	
	return check	

#/login: 判断用户名和密码是否与数据库中的相同
def check_login(username, password):
	u = 'sc___'+username+'___cs'
	p = inverse(password)
	#print u,p
	kv = sae.kvdb.Client()
	pw_list = [i for i in kv.get_by_prefix(u)]
	check = False
	if pw_list:
		pw_stored = reduce(pw_list, pw_list)[1]
		#print pw_stored
		if p == pw_stored:
			check = True
	return check

#倒转string
def inverse(anystr):
	newstr=''
	for i in anystr:
		newstr = i+newstr
	return newstr

#用户注册界面
@app.route('/newuser')
def newuser(information=''):
	return template('reg',information='')

@app.route('/newuser', method = 'POST')
def do_newuser():
	username = unicode(request.forms.get('username')).encode('ascii')
	keyun = 'sc___'+username+'___cs'
	password = request.forms.get('password')
	confirm = request.forms.get('confirm')
	if checkdup(keyun):
		return template('reg', information='该用户名已存在！')
	elif password == confirm:
		valpw = inverse(password)
		kv = sae.kvdb.Client()
		kv.add(keyun, valpw)
		redirect('/login') 
	else:
		return template('reg', information='请确保两次输入的密码相同！')

#用户登录界面
@app.route('/login')
def login():
	return template('login', information='')

@app.route('/login', method = 'POST')
def do_login():
	username = unicode(request.forms.get('username')).encode('ascii')
	password = request.forms.get('password')
	if check_login(username, password):
		response.set_cookie('account',username, secret='somekey')
		redirect('/')
	else:
		return template('login', information='登录失败，请确认用户名和密码，或注册新账号')

#所有标题显示/添加界面
@app.route('')
@app.route('/', method='get')
def allstory():
	user = request.get_cookie('account', secret='somekey')
	if not user:
		user = '游客'
	kv = sae.kvdb.Client()
	titleplus = kv.getkeys_by_prefix('sct___')
	title = {i[6:-20] for i in titleplus}
	print title
	output = template('allstory', userid=user, rows = title, information='')
	if request.GET.get('save'):
		newtitle = unicode(request.GET.get('title')).encode('utf-8')
		key_newtitle = 'sct___'+newtitle+'___tcs'
		if user == '游客':
			output = template('allstory', userid=user, rows = title, information='请登录')
		elif newtitle[0:5]=='sct___':
			output = template('allstory', userid=user, rows = title, information='不可以以“sct___”作为故事名')
		elif checkdup(key_newtitle):
			output = template('allstory', userid=user, rows = title, information='重名，请重新输入')
		else:
			newurl='/'+newtitle
			redirect (newurl)
	return output

#单个文档显示/输入界面
@app.route('/:name', method='GET')
def body(name):
	kv = sae.kvdb.Client()
	title = name
	key_title='sct___'+title+'___tcs'
	showcontent = [i for i in kv.get_by_prefix(key_title)]
	output= template('make_table', title=title, rows = showcontent, information='')
	if request.GET.get('save'):
		new = unicode(request.GET.get('main'))
		if len(new)>4:
			currentT = datetime.now()
			ShowT = currentT.strftime('%Y-%m-%d %H:%M:%S')
			user = request.get_cookie('account',secret='somekey')
			body = [new, user, ShowT]
			title_stored = key_title+currentT.strftime('%Y%m%d%H%M%S')
			print title_stored
			kv.add(title_stored, body)
			showcontent=[i for i in kv.get_by_prefix(key_title)]
			print showcontent
			output = template('make_table', title=title, rows=showcontent, information='')
		else:
			output = template('make_table', title=title, rows=showcontent, information="输入太短（至少五个字）")
	return output

#储存备份
#kv=sae.kvdb.Client()
#key_title='sct___'
#key_user='sc___'
#list_stories = [i for i in kv.get_by_prefix(key_title)]
#list_users = [i for i in kv.get_by_prefix(key_user)]	
#stories = open('stories.txt','w+')
#users = open('users.txt', 'w+')
#pprint(list_stories, stories)
#pprint(list_users, users)

#CSS, images
@app.route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root = '/path')
	
application = sae.create_wsgi_app(app)