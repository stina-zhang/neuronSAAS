#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

account = Element('account')
class AccountPage(WebPage):


    def input_account_password(self, content):
        """输入用户密码"""
        self.input_text_no_clear(account.密码输入框, content)

    def click_password_display(self):
        """密码显示或隐藏"""
        self.is_click(account.密码显示)

    def clear_account_password(self):
        self.is_click(account.密码输入框)

    def double_account_password(self):
        self.double_click(account.密码输入框)

    def input_account_nickname(self, content):
        """输入用户昵称"""
        self.input_text(account.昵称输入框, content)

    def input_account_phone(self, content):
        """输入用户联系电话"""
        self.input_text(account.联系电话输入框, content)

    def input_account_email(self, content):
        """输入用户邮箱"""
        self.input_text(account.邮箱输入框, content)

    def input_account_url(self, content):
        """输入用户回调url"""
        self.input_text(account.回调url输入框, content)

    def click_select_sex(self):
        """修改性别为女"""
        self.is_click(account.性别选择框)

    def click_save(self):
        """保存"""
        self.is_click(account.保存)

    def click_confirm(self):
        """确定"""
        self.is_click(account.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(account.取消)

    def click_quit(self):
        """退出页面"""
        self.is_click(account.退出)