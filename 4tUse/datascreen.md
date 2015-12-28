#####一个数据筛选的小程序
- 题目：
  - 某疾病组女性A月经失调比例高于对照疾病组B。这是一个值得报道的结果。但是，A组女性的年龄也显著低于B组。
  - 已知年龄会对月经规律性造成影响，那么A组的阳性结果是否是因为年龄差异呢？
- 设想：
  - 为了回答这一问题，最好能找到年龄差异不大的人群进行比较。
  - 因此，我设想用程序随机删除A组中年龄较小的患者，使得两组最终年龄差距在不显著的程度，再观察两组是否存在差异
- 实现随机删除的手段：
  - 为A组设立随机数，然后再符合条件的病例中，删除随机数最小的一个。
- 工具（痛点）：
  - mysql数据库
  - numpy统计处理，mean
  - scipy统计处理，t-test
  
- mysql的问题在于数据类型“？”，“%s”，“%d（大误）”，“%r（大误）”等，傻傻搞不清楚
 - 初学总结，不管什么数据类型，一律“%s”，最不易出错。

- numpy/scipy的安装
  - （win10/python2.7）
  - pip install numpy报错Unable to find vcvarsall.bat，找不到microsoft visual c++
  - 尝试过多种办法如
    - 安装microsoft visual c++ compiler package for python27
	- 安装打包的数据分析包Anaconda（大误，不能与原来的python一起用）
	- 下载numpy包手动安装
	- 更改VS90COMNTOOLS的指向等，都没有用。
	- 最后发现下面这个方法可行：
      - After doing a lot of things, I upgraded pip, setuptools and virtualenv.

	        python -m pip install -U pip
	        pip install -U setuptools
	        pip install -U virtualenv
      - I did steps 1, 2 in my virtual environment as well as globally. Next, I installed the package through pip and it worked.

    - scipy安装使用pip也报错，说是还缺少两个重要组件。觉得太麻烦，于是直接下载了win版的安装程序，安装成功。
	  - [下载地址](http://sourceforge.net/projects/scipy/files/scipy/)
- 运行
  - 大概删除了A组54-56个患者后（意味着仅保留了30个左右），两组差异的p值小于0.3
  
- 有待改进
  - 仅将年龄数据代入测试，下一步需要将其他关键数据代入，便于直接观察所测指标
  - 将被删除的患者代号、删除后结果保存到文件  
    
    	import csv
	    import MySQLdb
    	import random
    	db = MySQLdb.connect(host='localhost',
	    	user = 'root', passwd='Sww6416!')
    	cur=db.cursor()
    	cur.execute('CREATE SCHEMA IF NOT EXISTS HMage')
    	cur.execute('USE HMage')
	    cur.execute('DROP TABLE IF EXISTS HM_age')
    	cur.execute('''CREATE TABLE HM_age
	    	(
	    	No INTEGER NOT NULL PRIMARY KEY,
	    	Tag CHAR(1) NOT NULL,
	    	age FLOAT NOT NULL,
	    	randomnumber FLOAT 
	    	)''')

    	HMagedata = csv.reader(file('HMscreen.csv'))
    	for row in HMagedata:
	    	No = int(row[0])
		    Tag = row[1]
		    age = float(row[2])
	    	randomnumber = random.random()
	    	cur.execute('''INSERT INTO HM_age (No, Tag, age,randomnumber)
		    	VALUES(%s,%s, %s, %s)''',
			    (No, Tag, age,randomnumber))
    	cur.execute('SELECT age FROM HM_age WHERE Tag=%s','M')
    	list_M = cur.fetchall()

    	cur.execute('SELECT age FROM HM_age WHERE Tag=%s','H')
    	list_H = cur.fetchall()

    	count = 0
    	from numpy import mean
    	from scipy.stats import ttest_ind
	    while True:
		    t, p = ttest_ind(list_H, list_M)
		    print t, p
	    	if p>0.3:
	    		break
	    	elif t>0:
	    		Mmean = mean(list_M)
		    	print Mmean
		    	cur.execute('SELECT No FROM HM_age WHERE Tag="M" AND     age<%s ORDER BY randomnumber',(Mmean,))
		    	deleterow=cur.fetchone()
			    count += 1
			    print 'round',count,'delete',deleterow
			    cur.execute('DELETE FROM HM_age WHERE No = %s',(deleterow[0]))
			    cur.execute('SELECT age FROM HM_age WHERE Tag="M"')
			    list_M = cur.fetchall()
    	print mean(list_H),mean(list_M)	
	    db.commit()
	    cur.close()	  