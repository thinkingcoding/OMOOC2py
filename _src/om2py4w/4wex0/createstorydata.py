import sqlite3
fn = 'storychain.db'
cnct = sqlite3.connect(fn)
cnct.execute('''CREATE TABLE chains
	(title char(20) NOT NULL,
	ct INTEGER,
	main char(400) NOT NULL, 
	userid text,
	datetime text)
	''')
cnct.execute('''INSERT INTO chains VALUES 
	("wolf", 
	0,
	"There was once a boy-wolf.",
	"wwshen",
	"2015-11-15 15:00:00")
	''')
cnct.execute('''INSERT INTO chains VALUES 
	("wolf", 
	1,
	"He liked walking and dancing in the rain.",
	"wwshen",
	"2015-11-15 15:00:00")
	''')
cnct.execute('''INSERT INTO chains VALUES 
	("my dad", 
	0,
	"My dad is awesome!",
	"wwshen",
	"2015-11-15 15:00:00")
	''')
cnct.commit()