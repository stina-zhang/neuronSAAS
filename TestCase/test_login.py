#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from common.readconfig import conf
from utils.log import log
import yaml
from ddt import ddt, data, unpack, file_data
import time
from selenium.webdriver.support.ui import WebDriverWait



@ddt
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_domilogin(self, drivers):
        """打开domi登录页面"""
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)


    def test_001(self):
        """正常登录"""
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(2)
        newtitle = self.login.getTitle()
        logintitle = '多米+SAAS管理平台'
        assert newtitle != logintitle


    @file_data('login_data.yaml')
    def test_002(self, **kwargs):
        """异常登录"""
        username = kwargs.get('username')
        password = kwargs.get('password')
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.click_login()
        time.sleep(2)
        newtitle = self.login.getTitle()
        assert newtitle == '多米+SAAS管理平台'

# if __name__ == '__main__':
#     pytest.main(['test_login.py'])
