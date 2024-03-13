#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

login = Element('login')
class LoginPage(WebPage):

    def input_username(self, content):
        """输入用户名"""
        self.input_text(login.用户名输入框, content)
        sleep(1)

    def input_password(self, content):
        """输入密码"""
        self.input_text(login.密码输入框, content)
        sleep(1)

    def click_login(self):
        """点击登录按钮"""
        self.is_click(login.登录框)
        sleep(3)

    def error_message(self):
        """获取登录错误文本"""
        return self.isElementText(login.登录提示)

    def click_message(self):
        """点击提示框按钮"""
        self.is_click(login.不再显示提示框)
        sleep(1)







