#用python将CSV转入Mysql
- csv是以逗号分隔的数据文件，可以用excel和文本软件查看
- Mysql是关系数据库。将csv格式的数据转入Mysql，可以方便数据的联合、提取和分析
- 一个数据库下可建立多个表单。
- 本文主要介绍创建数据库和表单的具体过程。

##过程
- 需要用到csv和MySQLdb两个模块
	import csv
	import MySQLdb

- 连接数据库
	db = MySQLdb.connect(host='localhost',
	user = 'root', passwd='Mypassword')
	cur=db.cursor()
	
- 创建数据库Demo
	cur.execute('CREATE SCHEMA IF NOT EXISTS Demo')
  - ‘IF NOT EXISTS’先检查Mysql里是否已经存在Demo表，如不存在，则创建。这个语句可以省略
  
- 创建表单T1  
	cur.execute('USE Demo')
	#cur.execute('DROP TABLE IF EXISTS T1') #用于卸掉旧表
	cur.execute('''CREATE TABLE T1
		(
		Sub INTEGER NOT NULL,
		Gender INTEGER, 
		Age FLOAT, 
		Education INTEGER,
		)''')
  - 表单各纵列分别是被试号-性别-年龄-教育程度

- 将csv格式数据转入。
- 假设数据为(无题头)
	1,1,30,12
	2,1,31,16
	3,1,19,12
	4,2,22,16
	...
  - 保存于工作目录下的General.csv	
- 读取
	Generaldata = csv.reader(file('General.csv'))
- 存入Mysql
	for row in Generaldata:
		cur.execute('''INSERT INTO T1
			VALUES(%s,%s,%s,%s)''',
			(row)
			)
	db.commit()	
  - 这里，row[0]为[1,1,30,12]。但若row[0]为[(1,),(1,),(30,),(12,)]亦不影响读取

- 基本流程就是这样。但实际操作中可能遇到各种问题。如
  1. 希望保留csv文件表头（即被试号，性别，年龄，教育程度）
  2. 文件有空缺数据

## 希望保留csv表头
- csv.reader()读取出来的并不是数列。因此如果用
	Generaldata = csv.reader(file('General.csv'))
	for row in Generaldata[1:]:
  - 会出现报错：
		TypeError: '_csv.reader' object has no attribute '__getitem__'
- 解决方法是将之转化为list
	for row in list(Generaldata)[1:]:

## 文件有空缺数据
- 如文件有空缺数据，转入Mysql时会报错，大意是数据类型不匹配（如不是整数）
- 这是因为安装Mysql时选择了严格匹配数据的模式
- 解决方法是找到Mysql的my.ini配置文件，将sql-mode的配置从
		# Set the SQL mode to strict
		sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
- 改为
		# Set the SQL mode to strict
		sql-mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
- 改完以后重启Mysql，数据输入成功。
- 检查数据库，发现缺省值被全部改为0.但这并非我们想要的：因为数据为0会给下一步统计造成麻烦，且会与一些本来为数值0的数据相混淆。
- 好在数据库数值本身是可以设为Null的。如何以最小代价实现呢？
  - 自己编写一个python函数：
		def usenull(list):
			rownew=()
			for i in list:
				if i=='':
				i= None
			rownew+=(i,)
			return rownew
  - 并将存入Mysql的语句改为：
		for row in list(Generaldata)[1:]:
		cur.execute('''INSERT INTO T1
			VALUES(%s,%s,%s,%s)''',
			usenull((row))
			)
		db.commit()	
  - 再次查看数据库，缺省值已显示为null