# -*- coding: utf-8 -*-
#qpy:helloworld.py
#qpy:kivy

try:
    import androidhelper as android
except ImportError:
    import android
droid = android.Android()
	
respond = droid.dialogGetInput("Hello", "What is your name?")
print respond
#输出：Result(id=1, result=u'wwshen', ero=None)
name = respond.result
if name:
	message = 'Hello, %s!' % name
else:#不输入直接按ok（空字符串''），或者按取消（None）都会返回这里
	message = 'Hey! %Username%!'
droid.makeToast(message)
