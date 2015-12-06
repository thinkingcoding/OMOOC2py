#####第五周 故事接龙 公网版 编写日志
- 本周任务：将极简日志/故事接龙从本地调试的网页版搬到公网上
- 选用新浪sae作为平台。sae是一个可免费支持应用的平台，当然，很多增值服务也是要收费的。
- 首先注册sae，直接用weibo号登录。
- 登录以后填写邮箱和设置密码，这一步的邮箱和密码作为git推送时的用户名和密码。
- 设置应用名和url:故事接龙，storychain, url: storychain.sinaapp.com
- [部署git](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html)
  - git仓库 https://git.sinacloud.com/storychain
		$ cd OMOOC2py/_src/om2py5w #转移到应用所在文件夹（OMOOC2py/_src/om2py5w/5wex0）的上一级文件夹
		$ git init 5wex0 #启动
		$ git remote add sae https://git.sinacloud.com/storychain #远程仓库
		$ cd 5wex0 #转移到应用所在文件夹
		$ git status #查看文件状态
		$ git add -A #将所有文件转为staged状态
		$ git commit -a #将所有staged文件转入commit状态
		$ git push sae master:1 #推送至远程仓库
- 现在，可以登入storychain.sinaapp.com进行查看。
- 如果代码无误，则网页已经可以正确显示。不过，一般来说，提示都是错误，无法打开网页。这时，可以在本地再次修改代码并推送。
  - sae 采用index.wsgi作为运行程序，因此，我们在提交前应该将主程序SL5.py改名为index.wsgi
- 远程调试非常麻烦，我们将使用本地调试。使用方法很简单，在powershell中输入如下代码
		pip install sae-python-dev   #安装本地调试应用
		cd OMOOC2py/_src/om2py5w/5wex0/   #应用所在文件夹
		dev_server.py   #运行本地index.wsgi, 注意，前面不加python
  - 在浏览器输入localhost:8080即可看到我们设置的网页。但本地调试和远程环境存在区别。比如本地调试中可以使用sqlite3数据库，但远程并不支持这一数据库，因此涉及到数据库的代码需要调整。
- 使用kvdb作为数据库。
  - kvdb采用key+value的格式储存数据，没有复杂的关系。调用时，利用key的前缀将需要的数据提取出。
    - 每一个key都是独一无二的
	- 有一些字符不能用于key，如空格键
	- key不可以是unicode,仅能为字节
	- value不仅可以是字符串，也可以是数列，即list。
	- value可以是unicode
  - 方便起见，所有的数据都使用kvdb，包括用户名密码、故事名、语句、时间、和写作者。
  - 将数据分为两大部分，一部分是用户名/密码；另一部分是故事名/语句时间作者。这两部分使用不同的前缀区分。
    - 用户名/密码：用户名为key，前缀{% raw %}sc___,后缀___cs。{% endraw %}
      - 搜索某一用户名/密码时可以“前缀+用户名+后缀”作为prefix，保证所得唯一
      - 搜索所有用户时可以“前缀”作为prefix，以便提取所有用户信息
      - 下同	  
	- 故事名/语句时间作者：故事名为key，前缀为{% raw %}sct___,后缀1为___tcs{% endraw %}，后缀2为代表时间的数字串，后缀2是为了1）使每一个key都独一无二，2）方便排序。	
- key不可以是unicode
  - 需要将相关的语句用mystring.encode('utf-8')转回utf-8，e.g.:
		title = '我爱我家'
		time = '201512121212'
		key_title = 'sct___'+title.encode('utf-8')+'___tcs'+time
- key不接受空格等其他保留字符
  - 尚未处理这一问题。因此标题输入空格会导致出错。
- key/value的显示
		output=[i for i in getkeys_by_prefix('sct___') #产生所有标题的数列
		output=[i for i in get_by_prefix('sct___')] #产生具有标题（key）和value数列（语句，时间，作者）的复合数列
		                                            #其中每一组中，key为row[0]，语句为row[1][0], 时间为row[1][1], 作者为row[1][2]
- 动态url的问题
  - 创建新故事会用到动态url（根据使用者的命名产生相应的url）
  - 在本地，（python/bottle）使用{% raw %}@route('/<new>'){% raw %}，new为一个变量，可以正常显示。但sae中不支持，仅支持@route('/:new')。  

- 其他遗留问题
  - 仍不支持CLI
  - 未处理备份工作
  
- ps：sae实名问题
  - sae实名需要提交一张手持本人身份证的变态自拍照片。但是不实名将会影响微信后台的搭建。  
  