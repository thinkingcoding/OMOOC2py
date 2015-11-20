import sqlite3
users = 'users.db'
userdata = sqlite3.connect(users)
userdata.execute('''CREATE TABLE users
	(count INTEGER,
	userid char(20) NOT NULL,
	password char(20) NOT NULL)
	''')
#userdata.execute('INSERT INTO users VALUES (0, 'test', 'test')')	
#userdata.commit()
