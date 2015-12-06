##### 移动aap. 功能
- 本周整体任务概述:
  - 在之前开发基础上, 完成 极简交互式笔记的 移动应用 版本
  - 需求如下:
    - 推荐基于 QPython 快速构建:
    - 在手机端每次接收一行的文本(不包含表情/图片/声音/视频...)
    - 使用专用指令,可打印出过往所有笔记
    - 在服务端合理存储/管理
    - 同时兼容:
      - 命令行工具
      - 微信公众号
    - 可以通过本地命令行工具监察/管理 移动应用 运行:
    - 获得当前笔记数量/访问数量等等基础数据
    - 可以获得所有笔记备份的归档下载
  - 时限: 6wd4~7wd4
  - 发布: 发布到各自仓库的 _src/om2py7w/7wex0/ 目录中
  - 指标:
    - 包含软件使用说明书: README.md
    - 能令其它学员根据说明书,部署/运行/调试/增强系统
  - 备选的:
    - 如果有余力!-)
    - 请尝试:
      - 如何编译为标准 .apk 进行发布?
      - 如何建立认证功能,防止有人误入?
      - 如果识别weibo用户呢?
      - 即,这是一个私人笔记系统,不接受其它人使用
      - 当然,想作成多人也是相同的技术.
      - 如何建立数据加密?防止有人通过分析网络协议伪造数据提交?

###### 移动 app. QPy
- 什么是 Web app. ?
- 如何在 Android 手机上构建 Web App.?
- 都有什么姿势?
- 各有什么优点/缺点?
- 参考
  - [Web Apps | Android Developers](http://developer.android.com/guide/webapps/index.html)
    - [Installable Web Apps with the WebApp Manifest in Chrome for Android | Web Updates - Google Developers](https://developers.google.com/web/updates/2014/11/Support-for-installable-web-apps-with-webapp-manifest-in-chrome-38-for-Android)
  - [QPython Community - Home of QPythoners](http://qpython.org/)

###### 移动 app. 调试
- 什么是 QPython ?
- 如何基于 QPython 快速开发一个 Web App.?
- 能在桌面端进行开发嘛?
- 如何快速部署到手机上进行测试?
- 参考
  - Welcome to Fabric! — Fabric documentation](http://www.fabfile.org/)
  - QPython Community - Home of QPythoners

###### 移动 app. DB
- 如何基于 QPython 在手机中合理缓存数据?
- Android 环境中都有什么数据管理形式?
- 各有什么优点?缺点?
- 参考
  - 11.11. bsddb — Interface to Berkeley DB library — Python 2.7.11rc1 documentation](https://docs.python.org/2.7/library/bsddb.html)
  - 11.13. sqlite3 — DB-API 2.0 interface for SQLite databases — Python 2.7.11rc1 documentation](https://docs.python.org/2.7/library/sqlite3.html)
  - 11.4. shelve — Python object persistence — Python 2.7.11rc1 documentation](https://docs.python.org/2.7/library/shelve.html)
  - 11.5. marshal — Internal Python object serialization — Python 2.7.11rc1 documentation](https://docs.python.org/2.7/library/marshal.html)
  - QPython Community - Home of QPythoners

###### 移动 app. 发行
- 基于 QPython 完成开发后,如何分发给朋友们?
- 能编译为 .apk 嘛?
- 如何进行?!
- 如何不能,如何能令朋友们一键完成部署?
- 参考
  - QPython Community - Home of QPythoners