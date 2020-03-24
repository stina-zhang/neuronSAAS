#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element
from common.readconfig import conf
import time
from selenium import webdriver

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

    # @property
    # def imagine(self):
        # """搜索联想"""
        # return [x.text for x in self.findelements(search.搜索候选)]

    def click_login(self):
        """点击登录按钮"""
        self.is_click(login.登录框)
        sleep(3)

    def error_message(self):
        """获取登录错误文本"""
        return self.isElementText(login.登录提示)

    def get_username(self):
        """获取登录用户名"""
        return self.isElementText(login.用户名)

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     login1 = LoginPage(driver)
#     login1.get_url(conf.url)
#     login1.input_username('test2')
#     login1.input_password('123456')
#     login1.click_login()
#     print(login1.error_message())
#     print('123')





