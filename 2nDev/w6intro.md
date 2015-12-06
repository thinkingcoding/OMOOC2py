#####微信后台: 功能

- 本周整体任务概述:
  - 在之前开发基础上, 完成 极简交互式笔记的 微信后台 版本
  - 需求如下:
    - 将公网应用网站改写为公众号后台服务
    - 可以通过公众号使用:
    - 使用专用指令,可打印出过往所有笔记
    - 一次接收手机端输入的文字(不包含表情/图片/声音/视频...)
    - 在服务端合理保存
    - 同时兼容的命令行工具远程交互/使用/管理
    - 可以通过本地命令行工具监察/管理网站:
    - 获得当前笔记数量/访问数量等等基础数据
    - 可以获得所有笔记备份的归档下载
    - 时限: 5wd3~6wd3
  - 发布: 发布到各自仓库的 _src/om2py5w/6wex0/ 目录中
  - 指标:
    - 包含软件使用说明书: README.md
    - 能令其它学员根据说明书,部署/运行/调试/增强系统
  - 备选的:
    - 如果有余力!-)
    - 请尝试:
    - 如果分笔记类别呢?
    - 如何建立认证功能,防止有人误入?
    - 如果识别微信用户呢?
    - 即,这是一个私人笔记系统,不接受其它人使用
    - 当然,想作成多人也是相同的技术.
    - 如何建立数据加密?防止有人通过分析网络协议伪造数据提交

###### 微信后台: 公众号
- 如何创建一个公众号?
- 公众号和企业号的差别?
- 如何验证一个公众号服务器?
-参考
  - 微信公众平台开发者文档](http://mp.weixin.qq.com/wiki/home/index.html)
    - 接入指南 - 微信公众平台开发者文档](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html)
	
- 实践流程
  - 打开[微信公众平台官网](https://mp.weixin.qq.com/) -> 注册用户 ->邮箱确认 -> 选择订阅号（而非服务号/企业号），因为订阅号允许运营者为个人（服务号需要填写组织信息）->完善资料 ->点击并开启开发者中心 -> 写入url（storychain.sinaapp.com）-> token验证失败 -> google提示可能是sae未实名认证 ->转sae进行实名认证(需3天)。

###### 微信后台: 消息响应
- 微信各个终端的消息和公众号后台以及服务器的关系?!
- 消息的格式是 XML 的,什么是 XML ?
- 如何处理?!
- 参考
  - 微信公众平台开发者文档
    - 接收普通消息 - 微信公众平台开发者文档](http://mp.weixin.qq.com/wiki/17/fc9a27730e07b9126144d9c96eaf51f9.html)
  - 19.5. XML Processing Modules — Python 2.7.10 documentation](https://docs.python.org/2.7/library/xml.html)
    - 19.7. xml.etree.ElementTree — The ElementTree XML API — Python 2.7.10 documentation](https://docs.python.org/2.7/library/xml.etree.elementtree.html)

###### 微信后台: 指令设计
- 微信最常见使用情景是在手机上,那么什么样的指令最容易输入?!
- 用户的输入总是 chaos 的,那么:
- 如何人性/直觉的区分指令以及数据?
- 如果出错,如何指引用户?
- 参考
  - 微信公众平台开发者文档
    - 被动回复用户消息 - 微信公众平台开发者文档](http://mp.weixin.qq.com/wiki/18/c66a9f0b5aa952346e46dc39de20f672.html)
  - googleGood-API-DesignArmin Ronacher.pdf](http://zoomq.qiniudn.com/ZQCollection/pdf/google_Good-API-Design_Armin%20Ronacher.pdf)

###### 微信后台: 增强功能
- 大家都有微信, 应该能识别出用户来源的哪,具体怎么来?
- 一但能识别出用户,那么:
- 如何合理的分别存储不同用户的不同笔记?!
- 但是,如果大家想混在一起笔记交流呢?  
- 参考
  - 微信公众平台开发者文档
    - 获取用户基本信息(UnionID机制) - 微信公众平台开发者文档](http://mp.weixin.qq.com/wiki/17/c807ee0f10ce36226637cebf428a0f6d.html)
  - googleGood-API-DesignArmin Ronacher.pdf