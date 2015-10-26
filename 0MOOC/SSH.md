###用SSH替代Https
- window8.1, git bash 
- 2015-10-26
##### Https和SSH
  - 在使用git时可以发现SSH连接较Https更有优势
    - Https
      - 连接慢
      - 需输入密码
    - SSH
      - 连接快
      - 无需密码
##### 如何设置？  
  按照https://help.github.com/articles/generating-ssh-keys/ 设置
  - 全部在git bash下操作
  - 查看SSH keys
			$ ls -al ~/.ssh
    - 查看是否有id_rsa.pub、id_rsa等字样，如没有，则需创建SSH keys
  - 创建新SSH key 
			$ ssh-keygen -t rsa -b 4096 -C "你的github邮箱"
  - 出现Enter file in which to save the key字样，直接回车
  - 出现Enter passphrase字样，设置密码（注意设置时并不会出现任何字符）
  - 显示SSH key创建成功，会给出fingerprint和randomart image  
  - 将钥匙加入ssh-agent
    - 按教程
			$ ssh-agent -s
			SSH_AUTH_SOCK=/tmp/ssh-yb8QXSd4XOub/agent.956; export SSH_AUTH_SOCK;
			SSH_AGENT_PID=4444; export SSH_AGENT_PID;
			echo Agent pid 4444;

			$ ssh-add ~/.ssh/id_rsa 
			Could not open a connection to your authentication agent.
      - 显示无效
	- 因此搜索相关关键词，换用下列语句
			$ eval $(ssh-agent)
			$ ssh-add ~/.ssh/id_rsa
      -成功
	  -相关链接[stackoverflow](http://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent)
  - 将SSH key加入github账号
			$ clip < ~/.ssh/id_rsa.pub #将key复制到剪贴板
    - 登入github，点击个人头像下的settings，点击SSH keys，点击add SSH keys，在Title一栏，填入电脑描述（如dell PC win8等），在key一栏，ctrl+p粘贴。
	- 点击add key
	- 输入github密码
  - 测试连接
			$ ssh -T git@github.com 
    - 出现“Hi wwshen! You've successfully authenticated, but GitHub does not provide shell access.“显示成功。
  - 将https连接改为SSH连接
			$ git remote -v #显示网络仓库的地址
			$ git remote set-url origin git@github.com:[username]/[repository].git
			$ git remote -v #查看确认Https已经改为SSH
				
