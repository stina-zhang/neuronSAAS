#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from PageObject.rolepage import RolePage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time

class TestRole:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(0.5)
        self.index = Index(drivers)
        self.index.switch_role()

    def test_add_role_roolback(self, drivers):
        '''新增角色_撤销'''
        role = RolePage(drivers)
        role.switch_to_iframe()
        role.click_add()
        role.input_role_name("测试角色1")
        role.click_role_permission()
        role.click_select_all()
        role.click_role_permission()
        role.input_role_remark("测试角色备注1")
        role.input_role_code("5")
        role.click_rollback()
        role.swtich_to_default()
        role.click_confirm()

    def test_add_role(self, drivers):
        '''新增角色'''
        role = RolePage(drivers)
        role.switch_to_iframe()
        role.click_add()
        role.input_role_name("测试角色1")
        role.click_role_permission()
        role.click_select_all()
        role.click_role_permission()
        role.input_role_remark("测试角色备注1")
        role.input_role_code("5")
        role.click_save()
        role.swtich_to_default()
        role.click_confirm()
        role.click_confirm()
        role_add_name = operation_mysql().search_one(sql='SELECT * FROM user_role WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['name']
        assert role_add_name == "测试角色1"

    def test_edit_role_roolback(self, drivers):
        '''修改角色_撤销'''
        role = RolePage(drivers)
        role.switch_to_iframe()
        role.click_last_row()
        role.click_edit()
        role.input_role_remark("修改测试角色备注")
        role.click_rollback()
        role.swtich_to_default()
        role.click_confirm()
        role_add_name = operation_mysql().search_one(sql='SELECT * FROM user_role WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['remark']
        assert role_add_name == "测试角色备注1"

    def test_edit_role(self, drivers):
        '''修改角色'''
        role = RolePage(drivers)
        role.switch_to_iframe()
        role.click_last_row()
        role.click_edit()
        role.input_role_remark("修改测试角色备注")
        role.click_save()
        role.swtich_to_default()
        role.click_confirm()
        role.click_confirm()
        role_add_name = operation_mysql().search_one(sql='SELECT * FROM user_role WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['remark']
        assert role_add_name == "修改测试角色备注"


    def test_del_role_roolback(self, drivers):
        '''删除角色_撤销'''
        role = RolePage(drivers)
        role.switch_to_iframe()
        role.click_last_row()
        role.click_del()
        role.swtich_to_default()
        role.click_cancel()
        role_add_name = operation_mysql().search_one(sql='SELECT * FROM user_role WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['name']
        assert role_add_name == "测试角色1"

    def test_del_role(self, drivers):
        '''删除角色'''
        role = RolePage(drivers)
        role.switch_to_iframe()
        role.click_last_row()
        role.click_del()
        role.swtich_to_default()
        role.click_confirm()
        role.click_confirm()
        role_add_name = operation_mysql().search_one(sql='SELECT * FROM user_role WHERE flag=0 ORDER BY created DESC LIMIT 0,1')['name']
        assert role_add_name != "测试角色1"


# if __name__ == '__main__':
#     pytest.main(['test_role.py'])