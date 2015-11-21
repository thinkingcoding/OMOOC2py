######作业要求
- Web 101: 功能
- 本周整体任务概述:
  - 在上周开发基础上, 完成 极简交互式笔记的Web版本
  - 需求如下:
    - 通过网页访问系统:
    - 每次运行时合理的打印出过往的所有笔记
    - 一次接收输入一行笔记
    - 在服务端保存为文件
    - 同时兼容 3w 的 Net 版本的命令行界面进行交互

######实践
- 觉得如果很多人来写一个笔记的话很像故事接龙
- 出于当妈的天性，突然有点想做一个故事接龙的web
- 设想中主要包括两个页面，一个页面显示所有故事的题目和开头；另一个页面显示一个故事的所有接龙，包括作者和写入时间。当然，还要有注册和登录的界面。
- 照这个设想做，并没有考虑作业最后一点的内容，至今尚不知道如何兼容CLI
- ‘参考’了几个教程，分别是bottle的tutorial和bottle的to-do list tutorial

######故事接龙网站python编写教程
- 搭框架
  - 在纸上画出每个网页需要的内容
  - 四个网页分别为：
    - 用户注册界面@route('/newuser')
    - 用户登录界面@route('/')或@route('')或@route('/login')
	  - 即三个url都指向一个页面
    - 所有标题显示/输入新标题界面@route('/storychain')
    - 单个文档显示/输入新接龙界面@route('/storychain/<name>)
      - name为故事的标题

- 学习搭一个最基本的网页
		#引入要用到的功能
		from bottle import route, run
		@route('storychain/<name>) #动态可变的url
		def body(name=): #定义函数，默认
			return 'This is a story about{% raw %}{{name}}{% endraw %}.'#变量显示在{% raw %}{{}}{% endraw %}中
		run(host='localhost', port=8080)#()中不写同样可运行
  - 保存文件名为SL3.py到工作文件夹		
  - 在powershell中键入python SL3.py
  - 接着在浏览器中输入http://localhost:8080/storychain/wolf
  - 页面应显示: This is a story about wolf.

- 为方便调试，引入debug和reload
		from bottle import route, run
		from bottle import debug
		debug(True)
		@route('storychain/<name>)
		def body(name=): 
			return 'This is a story about{% raw %}{{name}}{% endraw %}.'
		run(host='localhost', port=8080, reloader= True)
  - 引入后程序的更改（保存后）会立即被运行并体现在网页中。

- 单个文档显示界面的制作
  - 接龙有哪些要素？
    - 接龙的句子，作者，创造时间、序号、以及标题
  - 文档保存在哪里？如何提取？
    - 我们使用sqlite3数据库作为存放所有故事的文件
  - 提取后如何展现在网页上？
    - 采用每行一句的方式，同时展现作者、创造时间、序号以及标题
  - 第一步，创建一个sqlite3数据库
		import sqlite3
		fn = 'storychain.db'#数据库文件名
		cnct = sqlite3.connect(fn)#创建并打开文件名
		cnct.execute('''CREATE TABLE chains 
			(title char(20) NOT NULL,
			ct INTEGER,
			main char(400) NOT NULL, 
			userid text,
			datetime text)
		''') #创建表格chains，chains的要素分别为title标题，ct计数，main接龙句，userid用户名和datetime时间
		cnct.execute('''INSERT INTO chains VALUES 
			("wolf", 
			0,
			"There was once a boy-wolf.",
			"wwshen",
			"2015-11-15 15:00:00")
		''')#安装以上顺序依次插入一行内容，便于调试（实际我插了三行）
  - 第二步，在def body()中按标题提取数据库的内容
		cnct = sqlite3.connect(fn)
		cc = cnct.cursor()
		t = (name,) #tuple
		cc.execute("SELECT * FROM chains WHEE title=？ ORDED BY ct", t)
		result = cc.fetchall() #list
  - 第三步，输出到页面		
		output = template('make_table', rows = result)#需要import bottle中的template
		return output
    - ‘make_table'是我们另外制作的模板文件，文件名为make_table.tpl，同样保存于工作文件夹
	- 'make_table'的内容如下，%左边是python语句，需要显示的变量在{% raw %}{{}}{% endraw %}中

			%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
			%<p>这个故事是这样的:</p>
			<table border="1">
			%for row in rows:
				<tr>
				%for col in row:
					<td>{{col}}</td>
				%end
				</tr>
			%end
			</table>
  - 第四步，准备输入界面
    - 直接在make_table中加上下面几句：

			<p>请你把故事接下去:</p>
			<form action='/storychain/{{title}}' method="GET">
			<input type="text" size="100" maxlength="400" name="main">
			<input type="submit" name="save" value="保存">
			</form>
    - 在def body()相应位置写入：
	
		if request.GET.get('save'):
			new = request.GET.get('main')#接龙句
			currentT = datetime.now()#需要from datetime import datetime
			ShowT = currentT.strftime('%Y-%m-%d %H:%M:%S') #时间显示
			user = request.get_cookie('account',secret='somekey')#当前用户
			cc.execute("SELECT ct FROM chains WHERE title=?", t)#提出该标题的计数
			ct = cc.fetchall()#提取了计数的队列{(1,),(2,),(3,)}
			ct = max(ct)#提取了最大的tuple(3,)
			New_ct = reduce(ct,ct) #转变为integer3
			New_ct += 1 #计数加1
			#将上述内容插入数据库表	
			cc.execute("INSERT INTO chains VALUES(?,?,?,?,?)", (unicode(name), New_ct, new,user,ShowT))
			conn.commit()
  - 基本框架完成

- 所有标题显示界面
  - 需展现要素：
    - 标题，首行接龙，进入单个故事页面的链接
  - 新建一个标题，跳转到相应页面
  - 第一步，框架
		@route('/storychain', method='get')
		def allstory():
			output = template('allstory', rows = ALL, information='')
			return output
  - 第二步，准备输出
		conn = sqlite3.connect(fn)#连接数据库
		cc=conn.cursor()
		#输出标题和首行（即计数为0）
		cc.execute("SELECT title, main FROM chains WHERE ct=?", (0,))
		#提取list
		ALL = cc.fetchall()
		conn.commit()
  - 第三步，加url，尝试过将其加入队列，当不能在页面正常显示，如下：
		ALLnew = []
		cnt=0
		for i in ALL:
			I = list(i)
			TITLE = I[0]
			url = "<a href='/"+TITLE+"'>Enter</a>"
			I.insert(2,url)
			i = tuple(I)
			ALLnew.insert(cnt,i)
			cnt += 1
  - 因此，直接将url体现在了模板中

			<b>浏览故事</b><p></p>
			%for row in rows:
				<b>{{row[0]}}:</b> 
				{{row[1]}}  ...
				<a href='/storychain/{{row[0]}}'>进入</a>
				<p></p>
			%end
    - 第三行row[0]为rows队列row tuple的第一个元素，即标题
	- 第四行row[1]为rows队列row tuple的第二个元素，即首行
	- 第五行将ow[0]转化成url
	- 第六行为换行
  - 第四步，准备输入
    - 在模板中写入
			<p>开始一个新故事:</p>
			<form action='/storychain' method='GET'>
				<input name='title' type='text' size = '20' maxlength='40'/>
				<input value = '创建' name = 'save' type = 'submit'/>
			</form>
    - 在def allstory()写入
		if request.GET.get('save'):
		newtitle = request.GET.get('title')#用户输入标题
		if check_title(newtitle):#检查是否有重名（另外定义）
			output = template('allstory', userid=user, rows = ALL, information='重名，请重新输入')
			return output
		else:
			newurl='/storychain/'+newtitle
			redirect (newurl)#转到单个故事页面

- 用户注册页面
  - 主要问题有
    - 用户名密码存放问题
    - 新用户名不能与原有用户名重名
    - 密码与再次输入密码要相同
    - 符合条件的记入数据库
    - post/get还一直搞得不清楚
  - 语句如下：
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
			if checkdup(alluser, username):#另外定义
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
  - 模板reg.tpl

			<form action = "/newuser" method = 'post'>
				请输入用户名: <input name = "username" type = "text"/>
				请输入密码: <input name = "password" type = "password"/>
				请再次输入密码：<input name = "confirm" type = "password"/>
				<input value = "提交" type="submit"/>
			</form>
			{{information}}

- 用户登录界面
  - 主要问题有
    - 用户名密码要与库中一致
  - 语句如下：
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
  - 模板略

- 几个函数
  - 判断用户名和密码是否与数据库中的相同
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

  - 判断标题是否重名
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
			
  - 判断注册重名
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

- 登录后在其他网页显示登录信息：cookie
  - 写入：
		response.set_cookie('acount', username, secret='somekey')
  - 读出
		request.get_cookie('account', secret='somekey')
  -*:需要from bottle import response, request

- 解决中文输入问题
	import sys
	reload(sys)
	sys.setdefaultencoding('utf8')
  - 并且，在相应的中文输入内容上加unicode(),如：
		newtitle = unicode(request.GET.get('title'))