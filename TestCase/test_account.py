#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from PageObject.accountpage import AccountPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time
import random

class TestAccount:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(0.5)
        self.index = Index(drivers)
        self.index.switch_account()

    def test_edit_account_nickname(self, drivers):
        '''修改昵称'''
        account = AccountPage(drivers)
        account.switch_to_iframe()
        NickName = "测试昵称" + str(random.randint(1,100))
        account.input_account_nickname(NickName)
        account.click_save()
        account.swtich_to_default()
        account.click_cancel()
        account.switch_to_iframe()
        account.input_account_nickname(NickName)
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        account.click_confirm()
        newAccountNickName = operation_mysql().search_one("SELECT * FROM user WHERE username='13800138001'")['nickname']
        assert newAccountNickName == NickName

    def test_edit_account_sex(self, drivers):
        '''修改性别'''
        account = AccountPage(drivers)
        AccountGender = operation_mysql().search_one("SELECT * FROM user WHERE username='13800138001'")['gender']
        account.switch_to_iframe()
        account.click_select_sex()
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        account.click_confirm()
        newAccountGender = operation_mysql().search_one("SELECT * FROM user WHERE username='13800138001'")['gender']
        assert AccountGender != newAccountGender

    def test_edit_account_phone(self, drivers):
        '''修改联系电话'''
        account = AccountPage(drivers)
        account.switch_to_iframe()
        user_phone = 13000000000 + random.randint(1000,9999)
        account.input_account_phone(user_phone)
        account.click_save()
        account.swtich_to_default()
        account.click_cancel()
        account.switch_to_iframe()
        account.input_account_phone(user_phone)
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        account.click_confirm()
        newAccountPhone = operation_mysql().search_one("SELECT * FROM user WHERE username='13800138001'")['phone']
        assert newAccountPhone == str(user_phone)

    def test_edit_account_email(self, drivers):
        '''修改邮箱'''
        account = AccountPage(drivers)
        account.switch_to_iframe()
        user_email = "105560" + str(random.randint(100,9999)) + "@163.com"
        account.input_account_email(user_email)
        account.click_save()
        account.swtich_to_default()
        account.click_cancel()
        account.switch_to_iframe()
        account.input_account_email(user_email)
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        account.click_confirm()
        newAccountemail = operation_mysql().search_one("SELECT * FROM user WHERE username='13800138001'")['email']
        assert newAccountemail == user_email

    def test_edit_account_url(self, drivers):
        '''修改邮箱'''
        account = AccountPage(drivers)
        account.switch_to_iframe()
        user_url = "http://www.domi100.com/api" + str(random.randint(100, 9999))
        account.input_account_url(user_url)
        account.click_save()
        account.swtich_to_default()
        account.click_cancel()
        account.switch_to_iframe()
        account.input_account_url(user_url)
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        account.click_confirm()
        newAccounturl = operation_mysql().search_one("SELECT * FROM user WHERE username='13800138001'")['cbUrl']
        assert newAccounturl == user_url

    def test_edit_account_password(self, drivers):
        '''修改密码'''
        account = AccountPage(drivers)
        account.switch_to_iframe()
        account.click_password_display()
        time.sleep(1)
        account.double_account_password()
        time.sleep(1)
        account.input_account_password("654321")
        time.sleep(1)
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        time.sleep(1)
        account.click_confirm()
        account.click_quit()
        account.click_confirm()
        login = LoginPage(drivers)
        login.input_username('13800138001')
        login.input_password('654321')
        login.click_login()
        login_user_name = login.get_username()
        assert login_user_name == '13800138001'
        #  密码改回到123456
        index = Index(drivers)
        index.switch_account()
        account.switch_to_iframe()
        account.click_password_display()
        time.sleep(1)
        account.double_account_password()
        time.sleep(1)
        account.input_account_password("123456")
        time.sleep(1)
        account.click_save()
        account.swtich_to_default()
        account.click_confirm()
        time.sleep(1)
        account.click_confirm()
        account.click_quit()
        account.click_confirm()

# if __name__ == '__main__':
#     pytest.main(['test_account.py'])
