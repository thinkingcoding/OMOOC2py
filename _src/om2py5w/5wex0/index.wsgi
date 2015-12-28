# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sae
import sae.kvdb
import MySQLdb


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
	
#情绪显示/新输入
@app.route('/imoodmap', method='get')
def moodmap():
	kv = sae.kvdb.Client()
	if request.GET.get('save'):
		newmood = unicode(request.GET.get('newmood'))
		level = int(request.GET.get('moodlevel'))
		story = unicode(request.GET.get('story'))
		currentT = datetime.now()
		Time = currentT.strftime('%Y%m%d%H%M%S')
		key_newmood = 'immmood___'+newmood.encode('utf-8')+'___mmi'+Time
		value_newbody = (newmood, level, story, currentT)
		kv.add(key_newmood, value_newbody)
	keylist = kv.getkeys_by_prefix('immmood___')
	#key为'immmood___'+情绪名+'___mmi'+系统时间
	moodname = {i[10:-20] for i in keylist}
	print moodname
	valuelist = kv.get_by_prefix('immmood___')
	#value是每组为（情绪名，情绪评分，故事，系统时间）的复合列表
	body = [i for i in valuelist]
	print body
	output = template('imm_main', rows = body)
	return output

#储存备份
@app.route('/backup')
def backup():
	kv=sae.kvdb.Client()
	key_prefix=('immmood___', 'sc___', 'sct___')
	for prefix in key_prefix:
		body = [i for i in kv.get_by_prefix(prefix)]
		data = open(prefix+'.txt','w+')
		pprint(body, data)
	kv.disconnect_all()
	return '备份成功'	

#imm测试
#@app.route('/imm/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root = "./imm/static/css")

#@app.route('/imm/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root ="./imm/static/js")

#@app.route('/imm/static/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root ="./imm/static/font-awesome")

#@app.route('/imm/font-awesome/<filepath:path>')
#def server_static(filepath):
#    return static_file(filepath, root ="./imm/font-awesome")


#@app.route('/imm/images/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/jpg')

#@app.route('/imm/images/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/png')

#@app.route('/imm/img/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/png')

#@app.route('/imm/img/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img', mimetype='image/jpg')

#@app.route('/imm/img/portfolio/<filename:re:.*\.png>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img/portfolio', mimetype='image/png')

#@app.route('/imm/img/portfolio/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img/porftolio', mimetype='image/jpg')

#@app.route('/imm/img/portfolio/<filename:re:.*\.jpeg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/img/portfolio', mimetype='image/jpeg')

#@app.route('/imm/static/img/<filename:re:.*\.jpg>')
#def send_image(filename):
#    return static_file(filename, root='./imm/static/img', mimetype='image/jpg')

#import mysqldb
mysql_host = "w.rdc.sae.sina.com.cn"
mysql_port = 3307
mysql_user = 'o1y13jokx4'
mysql_passwd = "zlw022313imm2jyy5iix0ml35hwi411khy41i5kl"
mysql_db = 'app_storychain'
#mysql_host = "localhost"
#mysql_port = 3306
#mysql_user = 'root'
#mysql_passwd = "Sww6416!"
#mysql_db = 'storychain'
	
@app.route('/imm')
@app.route('/imm/login')
def immlogin():
    return template('imm/imm_login', alertContent = "请登录，第一次见面直接登录注册")

@app.route('/imm/login', method ="POST")
def checkimmlogin():
	username = request.forms.get("studentname")
	print username
	pwd = request.forms.get('password')
	db = MySQLdb.connect(
		host =mysql_host, 
		port =mysql_port, 
		user =mysql_user, 
		passwd = mysql_passwd, 
		db= mysql_db
		)
	cursor =db.cursor()

	#check the username
	cursor.execute('SELECT name, AES_DECRYPT(password, "littleporkbun") FROM users WHERE name = %s', (username))
	checkname =cursor.fetchone()
	if checkname:
		if pwd == checkname[1]:
			return template('imm/index1', studentname = username)
		else:
			return template('imm/imm_login', alertContent = "亲，密码错误，放轻松，请再次输入！")
	else:
		cursor.execute('''
			INSERT INTO users(name,password) 
			VALUES(%s, AES_ENCRYPT(%s, "littleporkbun"))''',
			(username, pwd)
			)
	cursor.close()
	db.commit()
	return template('imm/index1', studentname = username)



@app.route('/imm/index')
def mainpage():
    return template('imm/index1',studentname = "imm")

@app.route('/imm/index',method ='POST')
def editform():
	studentName = request.forms.get('username')
	emotionType =request.forms.get('emotionType')
	flowValue =int(request.forms.get('flowValue'))
	tpFeeling =int(request.forms.get('tpFeeling'))
	tireness =int(request.forms.get('tireness'))
	diaryContent =request.forms.get('diaryContent')
	print studentName, emotionType, flowValue, tpFeeling, tireness, diaryContent
	db = MySQLdb.connect(
		host =mysql_host, 
		port =mysql_port, 
		user =mysql_user, 
		passwd = mysql_passwd, 
		db= mysql_db
		)
	cursor =db.cursor()

	cursor.execute('SELECT id FROM users WHERE name =%s', (studentName))
	users_id = cursor.fetchone()[0]
	print users_id
	cursor.execute('SELECT id FROM moodtype WHERE type =%s', (emotionType))
	moodtype_id = cursor.fetchone()[0]
	print moodtype_id
	print moodtype_id+users_id
	print flowValue+tpFeeling+tireness
	time=datetime.now()
	cursor.execute('''INSERT INTO records 
		(content,flow, tiredness, physicalcomfort,users_id,moodtype_id)
		VALUES(%s,%r, %r, %r,%r,%r)
		''', 
		(diaryContent,flowValue, tireness, tpFeeling, users_id, moodtype_id))
	cursor.close()
	db.commit()



@app.route('/imm/echarts')
def echarts():
    counttypes =[2,4,6,8,10]
    return template('imm/echarts', countTypes = counttypes)

@app.route('/imm/echarts_pie')
def echarts_pie():
    counttypes =[2,4,6,8,10]
    return template('imm/echarts_pie', countTypes = counttypes) 



	
application = sae.create_wsgi_app(app)



