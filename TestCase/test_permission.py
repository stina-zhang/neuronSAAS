#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from PageObject.primissionpage import PermissionPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time

class TestPermission:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(0.5)
        self.index = Index(drivers)
        self.index.switch_peimission()

    def test_add_permission_roolback(self, drivers):
        '''新增权限_撤销'''
        permission = PermissionPage(drivers)
        permission.switch_to_iframe()
        permission.click_add()
        permission.input_permission_name("测试权限")
        permission.input_permission_remark("测试权限备注")
        permission.input_permission_code("16384")
        permission.click_rollback()
        permission.swtich_to_default()
        permission.click_confirm()

    def test_add_permission(self, drivers):
        '''新增权限'''
        permission = PermissionPage(drivers)
        permission.switch_to_iframe()
        permission.click_add()
        permission.input_permission_name("测试权限")
        permission.input_permission_remark("测试权限备注")
        permission.input_permission_code("16384")
        permission.click_save()
        permission.swtich_to_default()
        permission.click_confirm()
        permission.click_confirm()
        permission_add_name = operation_mysql().search_one(sql='SELECT * FROM user_permission WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['name']
        assert permission_add_name == "测试权限"

    def test_edit_permission_roolback(self, drivers):
        '''修改权限_撤销'''
        permission = PermissionPage(drivers)
        permission.switch_to_iframe()
        permission.click_last_row()
        permission.click_edit()
        permission.input_permission_remark("修改测试角色备注")
        permission.click_rollback()
        permission.swtich_to_default()
        permission.click_confirm()
        permission_add_remark = operation_mysql().search_one(sql='SELECT * FROM user_permission WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['remark']
        assert permission_add_remark == "测试权限备注"

    def test_edit_permission(self, drivers):
        '''修改权限'''
        permission = PermissionPage(drivers)
        permission.switch_to_iframe()
        permission.click_last_row()
        permission.click_edit()
        permission.input_permission_remark("修改测试权限备注")
        permission.click_save()
        permission.swtich_to_default()
        permission.click_confirm()
        permission.click_confirm()
        permission_edit_remark = operation_mysql().search_one(sql='SELECT * FROM user_permission WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['remark']
        assert permission_edit_remark == "修改测试权限备注"


    def test_del_permission_roolback(self, drivers):
        '''删除权限_撤销'''
        permission = PermissionPage(drivers)
        permission.switch_to_iframe()
        permission.click_last_row()

        permission.click_del()
        permission.swtich_to_default()
        permission.click_cancel()
        permission_name = operation_mysql().search_one(sql='SELECT * FROM user_permission WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['name']
        assert permission_name == "测试权限"

    def test_del_permission(self, drivers):
        '''删除权限'''
        permission = PermissionPage(drivers)
        permission.switch_to_iframe()
        permission.click_last_row()
        permission.click_del()
        permission.swtich_to_default()
        permission.click_confirm()
        permission.click_confirm()
        permission_name = operation_mysql().search_one(sql='SELECT * FROM user_permission WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['name']
        assert permission_name != "测试权限"


# if __name__ == '__main__':
#     pytest.main(['test_permission.py'])
