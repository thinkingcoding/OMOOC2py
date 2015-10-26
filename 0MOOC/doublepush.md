###实现gitbook和github的双推
+ 即将本地仓库的更新同步到gitbook和github
+ 2015-10-26
+ window8.1

#####为什么有双推的问题
- gitbook提供了一个网络分享平台。用gitbook架设和书写电子书，可以使人的思维得到锻炼——更加地系统化。
- github作为一个程序员仓库，可储存日常数据（包括我们在gitbook上的更新）。同时也是程序员日常交流的重要平台。
- gitbook与github联动，意味着我们可以减少分别更新两个网站的机械操作，同时降低发生错误的可能。
- gitbook网站提供与github联动的操作，但按其操作流程，需要首先在gitbook创建书本，再将书本仓库输入github（创建新仓库）
- 而我们想做的，则是先在github先建立个人分支（fork）仓库，然后把它载入gitbook，从而创建有模板框架的电子书。但这种方式无法将gitbook的内容自动同步到github


#####如何双推
######预热
- 在进行操作之前，了解什么是git和git的基本命令是必要的。
  - 熟悉常用的git命令
			git config --global user.name 
			git config --global user.email
			git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multInst -nossession"
			git clone [url]
			git init [repository name]
			git status
			git add
			git commit
			git fetch #fetch but do not merge
			git pull #fetch and merge
			git push [remote-name] [branch-name] # git push origin master
			git remote -v
    - []表示个性化内容，语句书写时不用写"[]"
- 在进行操作之前，了解gitbook的仓库书写规则
			https://git.gitbook.com/[username]/[bookname].git
  - 如我的仓库为https://git.gitbook.com/wwshen/omooc2py.git
  - 注意大小写

######操作
- 参考[双推教程](https://openmindclub.gitbooks.io/omooc-py/content/support/dpush.html) 
- 创建好github仓库（如wwshen/OMOOC2py）和gitbook图书（用户名wwshen，图书名omooc2py）
- 将github仓库clone到本地 c:/shen
- 可以看到c:/shen/OMOOC2py/.git/config有以下配置声明
		[remote "origin"]
		url = git@github.com:wwshen/OMOOC2py.git
		fetch = +refs/heads/*:refs/remotes/origin/*
- 将其增改为
		[remote "book"]
		url = https://git.gitbook.com/wwshen/omooc2py.git
		fetch = +refs/heads/*:refs/remotes/origin/*
	[remote "hub"]
		url = git@github.com:wwshen/OMOOC2py.git
		fetch = +refs/heads/*:refs/remotes/origin/*
	[remote "origin"]
		url = git@github.com:wwshen/OMOOC2py.git
		fetch = +refs/heads/*:refs/remotes/origin/*
- 回到仓库根目录，测试
		$ git remote -v
		显示如下：
		book    https://git.gitbook.com/wwshen/omooc2py.git (push)
		book    https://git.gitbook.com/wwshen/omooc2py.git (fetch)
		hub git@github.com:wwshen/OMOOC2py.git (push)
		hub git@github.com:wwshen/OMOOC2py.git (fetch)
		origin  git@github.com:wwshen/OMOOC2py.git (push)
		origin  git@github.com:wwshen/OMOOC2py.git (fetch)
- 配置明文口令，以便不用输入用户名密码，即将以上remote book中的内容改为
		[remote "book"]
		url = https://wwshen:[我的密码]@git.gitbook.com/wwshen/omooc2py.git
		fetch = +refs/heads/*:refs/remotes/origin/*
- 同步与双推
  - 因为本人的gitbook已经有不少内容，而且并未同步到本地，因此第一步是将gitbook的更新拉回本地
			git pull book master
  - 然后推送
			git push book master
			git push origin master
		