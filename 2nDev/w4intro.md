#####第四周作业 教练引导
- Web 101: 功能
- 本周整体任务概述:
  - 在上周开发基础上, 完成 极简交互式笔记的Web版本
  - 需求如下:
    - 通过网页访问系统:
    - 每次运行时合理的打印出过往的所有笔记
    - 一次接收输入一行笔记
    - 在服务端保存为文件
    - 同时兼容 3w 的 Net 版本的命令行界面进行交互
  - 时限: 3wd4~4wd3
  - 发布: 发布到各自仓库的 _src/om2py4w/4wex0/ 目录中
  - 指标:
    - 包含软件使用说明书: README.md
    - 能令其它学员根据说明书,运行系统,完成所有功能
  - 备选的:
    - 如果有余力!-)
    - 请尝试: 将消息放到数据库中呢?
    - 哪种数据库?
    - 自制数据库?
    - 内建库支持哪些种类的数据库?

- 框架
  - 推荐使用 Bottle 框架来快速完成原型:
  - 发布一个网站
  - 可以接收用户输入
  - 可以动态将用户输入打印回网页
 
- 参考:
  - 什么是框架?为什么有框架？
    - [什么是web框架](http://www.cnblogs.com/hazir/p/what_is_web_framework.html)
  - Python 世界中有哪些框架?
    - [python有哪些好的web框架？](http://www.zhihu.com/question/20706333)
	- [浅谈五大python web框架](http://www.csdn.net/article/2011-02-17/292058)
  - 为什么大妈推荐 Bottle?
    - 参考对于众框架的介绍，主要原因：精简
	- [python+bottle+sina SAE快速构建网站](http://www.cnblogs.com/Xjng/p/3511983.html)
  - [Bottle: Python Web Framework — Bottle 0.13-dev documentation](http://bottlepy.org/docs/dev/index.html)	

- 模板
  - Bottle 内置的模板非常简单,简单到什么都要自个儿撸
  - 那么使用现成的模板系统来美化网站吧!
  - 参考
    - 什么是模板?
	  - Templating, and in particular web templating is a way to represent data in different forms. These forms often (but not always) intended to be readable, even attractive, to a human audience. Frequently, templating solutions involve a document (the template) and data. Template usually looks much like the final output, with placeholders instead of actual data (or example data in simplified form), bears common style and visual elements. Data which is presented using that template may be also separated in two parts - data required to be rendered, and data required for template itself (navigation elements if it is a site, button names if it is some UI). Combining template+data produces the final output which is usually (but not always) a web page of some kind.
	  - from [Templating in python](https://wiki.python.org/moin/Templating)
    - 为什么有模板?
    - Python 世界中有哪些模板?
	  - [Python web 模板框架](http://simple-is-better.com/sites/template)
    - 为什么大妈推荐 Jinja2?
	  - [python web开发：几个模板系统的性能对比](http://blog.chedushi.com/archives/910)
	- [Jinja2 (The Python Template Engine)](http://jinja.pocoo.org/)
	- [中文教程](http://docs.jinkan.org/docs/jinja2/#jinja2)

- 样式
  - 网站的美化是没有极限的!
  - 但是,我们有什么方法可以用最小成本美化到足够拿出手?
  - 参考
    - Bootstrap · The world's most popular mobile-first and responsive front-end framework.
    - Bootstrap 的生态包含了什么?
    - 为什么 Bootstrap 如此受欢迎?
    - 有更加简洁的同类 样式 框架嘛

- DB
  - 网站能看了,但是,数据还在用文件就不够看了...
  - 嗯哼?! 为什么!?
  - 必须用数据库了,但是,还不会 SQL 怎么办?
  - 给我们的网站配置上一种 NoSQL 数据库吧!
  - 参考:
    - 什么是 NoSQL ?
    - NoSQL 分哪些种类?
    - 哪种最简单?
    - 如何策略数据库结构?
    - 如何迁移数据?
    - 如何备份?
    - 11.13. sqlite3 — DB-API 2.0 interface for SQLite databases — Python 2.7.10 documentation
    - 11.11. bsddb — Interface to Berkeley DB library — Python 2.7.10 documentation
    - kvdb
    - bottle-simple-todo / wiki / Home — Bitbucket