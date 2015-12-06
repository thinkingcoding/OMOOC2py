# -*- coding: utf-8 -*-
#qpy:simplegui.py
#qpy:kivy

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        # display a button with the text : Hello QPython
        return Button(text='Hello QPython')

TestApp().run()