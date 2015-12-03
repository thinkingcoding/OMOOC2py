#####w5ex0作业: PaaS 101

- 本周整体任务概述:
  - 在上周开发基础上, 完成 极简交互式笔记的 PaaS 版本
  - 需求如下:
    - 将上周应用网站发布为公网稳定服务
    - 可以通过固定域名访问系统:
    - 每次运行时合理的打印出过往的所有笔记
    - 一次接收输入一行笔记
    - 在服务端保存为文件
    - 同时兼容 3w 的 Net 版本的命令行界面进行交互
    - 可以通过本地命令行工具监察/管理网站:
    - 获得当前笔记数量/访问数量等等基础数据
    - 可以获得所有笔记备份的归档下载
  - 时限: 4wd4~5wd3
  - 发布: 发布到各自仓库的 _src/om2py5w/5wex0/ 目录中
  - 指标:
    - 包含软件使用说明书: README.md
    - 能令其它学员根据说明书,运行系统,完成所有功能
  - 备选的:
    - 如果有余力!-)
    - 请尝试:
      - 如果分笔记类别呢?
      - 如何建立认证功能,防止有人误入?
      - 即,这是一个私人笔记系统,不接受其它人使用
      - 当然,想作成多人也是相同的技术.
      - 如何建立数据加密?防止有人通过分析网络协议伪造数据提交

- PaaS 101: SAE
  - 首先,我们得有个固定的免费环境能开始运行/调试
  - 推荐 SAE
  - 为什么!?
  - 全球能免费运行 Python 应用网络的有哪些种 PaaS?
  - 什么是 PaaS ?
  - 为什么要用 PaaS 而不是 VPS?
  - [git推送](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html)
  - 参考
    - [Platform as a service - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Platform_as_a_service)
    - [新浪云](http://www.sinacloud.com/doc/sae/python/index.html)

- PaaS 101: Bottle
  - 在 SAE 中如何运行 Bottle 的应用!?
  - SAE 的技术支持如何获得?
  - 运行时服务端日志如何获得?
    - [新浪云-日志系统](http://www.sinacloud.com/doc/sae/python/runtime.html#id4)
      - 打印到stdout和stderr的内容会记录到应用的日志中心中，所以直接使用print语句或者logging模块来记录应用的日志就可以了。
      - 日志内容在 你的应用名»运维» 日志中心» HTTP 中查看，类别为debug。
  - 能在本地事先进行应用开发嘛!?
    - [新浪云 -相关工具 -本地开发环境](http://www.sinacloud.com/doc/sae/python/tools.html)
    -命令

		pip install sae-python-dev   #安装本地调试应用
		cd OMOOC2py/_src/om2py5w/5wex0/   #应用所在文件夹
		dev_server.py   #运行本地index.wsgi
		
- PaaS 101: KVDB
  - 终于有了稳定的公众网络服务发布点
  - 那么,可以比较长期的收集私人笔记了, 可是:
  - 如何分类收集?
  - 如何管理分类?
  - 如何备份?
  - 参考
    - [kvdb.新浪云](http://www.sinacloud.com/doc/sae/python/kvdb.html)
    - [pprint – Pretty-print data structures - Python Module of the Week](https://pymotw.com/2/pprint/index.html)

- PaaS 101: CLI
  - 那么,长期运行中的系统状态/访问统计...如何进行?!
  - 通过 CLI 远程进行非功能性接触时,如何设计接口?
  - 参考
    - [googleGood-API-DesignArmin Ronacher.pdf](http://zoomq.qiniudn.com/ZQCollection/pdf/google_Good-API-Design_Armin%20Ronacher.pdf)
    - [Simple API's with bottle.py](http://mysticcoders.com/simple_apis_bottlepy_presentation/#/)

