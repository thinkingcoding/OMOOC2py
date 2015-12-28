#-*- coding:utf-8 -*-
#author: WhaleChen

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from bottle import Bottle, run,template,request,debug

import sae
import sae.const
import MySQLdb
import time 


app=Bottle()

from bottle import static_file
@app.route('/imm/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root = "./imm/static/css")

@app.route('/imm/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root ="./imm/static/js")

@app.route('/imm/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root ="./imm/static/font-awesome")

@app.route('/imm/font-awesome/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root ="./imm/font-awesome")


@app.route('/imm/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./imm/img', mimetype='image/jpg')

@app.route('/imm/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./imm/img', mimetype='image/png')

@app.route('/imm/img/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./imm/img', mimetype='image/png')

@app.route('/imm/img/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./imm/img', mimetype='image/jpg')

@app.route('/imm/img/portfolio/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='./imm/img/portfolio', mimetype='image/png')

@app.route('/imm/img/portfolio/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./imm/img/porftolio', mimetype='image/jpg')

@app.route('/imm/img/portfolio/<filename:re:.*\.jpeg>')
def send_image(filename):
    return static_file(filename, root='./imm/img/portfolio', mimetype='image/jpeg')

@app.route('/imm/static/img/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='./imm/static/img', mimetype='image/jpg')

#import mysqldb
	
@app.route('/imm')
@app.route('/imm/login')
def immlogin():
    return template('imm/imm_login', alertContent = "请登录，第一次见面直接登录注册")

@app.route('/imm/login', method ="POST")
def checkimmlogin():
	username = request.forms.get('studentname')
	pwd = request.forms.get('password')
	db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="SAE_MYSQL_USER", passwd ="SAE_MYSQL_PASS", db="app_storychain")
	cursor =db.cursor()
	cursor.execute('USE app_storychain')

	#check the username
	cursor.execute('SELECT name, AES_DECRYPT(password, "littleporkbun") FROM users WHERE name = ?' ,(username,))
	checkname =cursor.fetchone()
	if checkname:
		if pwd == checkname[1]:
	        return template('imm/index1', studentname = username)
		else:
			return template('imm/imm_login', alertContent = "亲，密码错误，放轻松，请再次输入！")
	else:
		cursor.execute('''
			INSERT INTO users(name,password) 
			VALUES("%s", AES_ENCRYPT("%s", 'littleporkbun')''' 
			%(studentName,pwd)
			)
	cursor.close()
	db.commit()
	return template('imm/index1', studentname = studentName)



@app.route('/imm/index')
def mainpage():
    return template('imm/index1',studentname = "imm")

@app.route('/imm/editform',method ='POST')
def editform():
    studentName = request.forms.get('username')
    emotionType =request.forms.get('emotionType')
    flowValue =int(request.forms.get('flowValue'))
    tpFeeling =request.forms.get('tpFeeling')
    tireness =int(request.forms.get('tireness'))
    diaryContent =request.forms.get('diaryContent')
    db = MySQLdb.connect(host ="w.rdc.sae.sina.com.cn", port =3307, user ="SAE_MYSQL_USER", passwd ="SAE_MYSQL_PASS", db="app_storychain")
    cursor =db.cursor()
    cursor.execute('USE app_storychain')
	cursor.execute('SELECT id FROM users WHERE name = studentName')
	users_id = cursor.fetchone()[0]
	cursor.execute('SELECT id FROM moodtype WHERE type = emotionType')
	moodtype_id = cursor.fetchone()[0]
    cursor.execute('''INSERT INTO records 
		(content, flow, tiredness, physicalcomfort, moodtype_id, users_id)
		VALUES(?,?,?,?,?,?)
		''', 
		(diaryContent, flowValue, tireness, tpFeeling, moodtype_id, users_id))
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


		
debug(True)	
application =sae.create_wsgi_app(app)
