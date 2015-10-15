# git 私人教程

## 背景
+ git是一种版本管理工具。在写作、编程、图片制作等过程中，我们常常要比较、回溯不同的版本。这使得版本管理变得重要。简易的文本管理可以用时间命名等方式手动进行。但当版本众多，且出现系列分支文件时，我们往往陷入混乱，也常常出现误删等情况。git可以在本地和远程保留所有版本的文件，并在不同文件中对比差别、进行合并、回溯等操作。不仅方便了个人的版本管理，也会合作提供了便捷的工具。
+ git与其他版本管理工具的差别主要在于它储存每个版本所有文件的快照，而不是文件更改的索引。这使得它可以在本地存储所有的历史版本，而不仅是最新的版本。因此更加方便离线操作。

## 安装
 + 我的git for windows在git-scm.com下载，安装后显示三个程序，分别
是git cmd，git bash，和git gui。其中gui是人机交互界面（比较傻瓜），bash和cmd是命令输入界面。git的操作通常zaibash中进行。

 + 也可以在github上下载git，安装以后应显示两个程序，分别是git gui和git shell。这个版本的git 仅适用win7后的系统。但我的
电脑win8.1仍安装失败，提示是连接相关网址出错。具体原因尚未查证。

## 配置
+ win8.1/ 有时使用win xp

## 使用
+ 初始

 + 打开git bash

 + 设定用户名
        $ git config --global username "myname"

 + 设定邮箱
        $ git config --global user.email mymail@mailbox.com
 + 设定编辑器
        $ git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -nosession"
   + 注意Program Files和(x86)之间有一个空格！因为没有发现空格，我在后来的commit操作中失败了无数次。
   + git documentation上这么说：You may find, if you don’t setup an editor like this, you will likely get into a really confusing state when they are launched. Such example on a Windows system may include a prematurely terminated Git operation during a Git initiated edit.

 + 建立本地仓库
   + 因为已在github上建立了公共仓库，因此这里采用了直接复制github仓库的方式
            $ git clone https://github.com/myname/myrepo
   + 如果想在本机更改库名，则可以在命令后添加新名字
            $ git clone https://github.com/myname/myrepo newrepo
   + 新建仓库可以用 $ git init myrepo，同时这一命令还可以启动已存在的repo

- git中的几个重要概念：untracked tracked modified staged
![the lifecycle of the status of your files](https://git-scm.com/book/en/v2/book/02-git-basics/images/lifecycle.png)

+ 打开本地仓库
		$ git init myrepo
   + myrepo位于c/documents and settings/xxx(username)
   + 此命令也用于新建本地仓库
+ 检查文件状态
  + xp
		$ git status（或$ git status -s 或$ git status --short）
    + 这一命令把我位于c/documents and settings/xxx（即working directory）的所有文件都扫了出来，并将它们了列为untracked。
  + win8
    + 直接输入上述错误导致错误提示：fatal: Not a git repository (or any of the parent directories): .git
    + 此句是提示我目前不在正确的目录下（我在c:/documents and settings/xxx，正确的目录是c:/documents and settings/xxx/myrepo）
    + 更改为
			$cd myrepo
			$git status
+ 将untrack文件加入track(状态staged）
  + 将文件test.txt加入track（staged状态）
		$git add test.txt
		$git status 
     + 现在，test.txt处于staged状态（即已修改，待提交）
   
  + modified未staged状态
    + 修改test.txt，随后再次查看git status，显示test.txt位于modified的状态，但新改变没有staged（旧的test.txt仍处于staged的状态）
    + 再次使用git add使其进入staged的状态
			
+ 修改文件并commit
        $ echo here is a test from git bash >>myrepo/w1/README.md 
        $ git add w1/README.md
        $ git commit w1/README.md
  + 跳出Notepad++，提示“Please enter the commit message for your changes.”添加文字：this is a test for git commit and notepad++，保存并关闭。
  + 提示1 file changed, 1 insertion(+)
  + 此外有一个warning：LF will be replaced by CRLF in w1/README.md

## 体验

