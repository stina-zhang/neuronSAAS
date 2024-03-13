#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys

sys.path.append('.')
import pytest
# from py._xmlgen import html
from selenium import webdriver
from common.readconfig import conf
import time
from PageObject.loginpage import LoginPage

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    # 前置操作setup
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()

    def fn():
        # 后置操作teardown
        print("当全部用例执行完之后：quit driver！")
        driver.close()
    request.addfinalizer(fn)

    # 返回前置操作的变量
    return driver

@pytest.fixture(scope='session', autouse=True)
def open_loginhtml(drivers):
    login = LoginPage(drivers)
    login.get_url(conf.baseurl)
    login.input_username('root')
    login.input_password('yyds@neurons')
    login.click_login()
    login.click_message()
    time.sleep(0.5)


