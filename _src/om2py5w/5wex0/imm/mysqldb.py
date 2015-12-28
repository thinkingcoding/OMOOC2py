#-*- coding:utf-8 -*-
import sae
import sae.const
import MySQLdb
import time 

db = MySQLdb.connect(host ="localhost", port =3306, user ="root", passwd ="Sww6416!", db="storychain")
cursor =db.cursor()
cursor.execute('USE app_storychain')
cursor.execute('''CREATE TABLE IF NOT EXISTS users
	(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20) UNIQUE NOT NULL,
	password VARCHAR(20) NOT NULL
	)
	''')
cursor.execute('''CREATE TABLE IF NOT EXISTS moodtype
	(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	type VARCHAR(20) UNIQUE NOT NULL,
	)
	''')
cursor.execute('''INSERT INTO moodtype 
	(type)
	VALUES ('Joy')
	''')
cursor.execute('''CREATE TABLE IF NOT EXISTS records
	(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	time DATETIME NOT NULL,
	content TEXT(400),
	flow INTEGER(1),
	tiredness INTEGER(1),
	physicalcomfort INTEGER(1),
	moodtype_id INTERGER(1),
	users_id INTEGER
	)
	''')