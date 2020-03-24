#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from PageObject.agency import AgencyPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time
import allure

class TestAgency:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(0.5)
        self.index = Index(drivers)
        self.index.switch_agency()

    def test_add_agency_roolback(self, drivers):
        '''新增代理商_撤销'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_add()
        agency.input_agency_name("测试代理商1")
        agency.input_agency_remark("测试代理商备注")
        agency.click_rollback()
        agency.swtich_to_default()
        agency.click_confirm()

    def test_add_agency(self, drivers):
        '''新增代理商'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_add()
        agency.input_agency_name("测试代理商1")
        agency.input_agency_remark("测试代理商备注")
        agency.click_save()
        agency.swtich_to_default()
        agency.click_confirm()
        agency.click_confirm()
        newAgencyName = operation_mysql().search_one("SELECT username from `user` ORDER BY created DESC LIMIT 0,1")['username']
        assert newAgencyName == "测试代理商1"
        operation_mysql().close_sql()

    def test_edit_agency_roolback(self, drivers):
        '''修改代理商_撤销'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_row()
        agency.click_edit()
        agency.input_agency_remark("修改测试代理商备注")
        agency.click_rollback()
        agency.swtich_to_default()
        agency.click_confirm()
        newAgencyName = operation_mysql().search_one("SELECT username from `user` ORDER BY created DESC LIMIT 0,1")['username']
        assert newAgencyName == "测试代理商1"
        operation_mysql().close_sql()

    def test_edit_agency(self, drivers):
        '''修改代理商'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_row()
        agency.click_edit()
        agency.input_agency_remark("修改测试代理商备注")
        agency.click_save()
        agency.swtich_to_default()
        agency.click_confirm()
        agency.click_confirm()
        newAgencyRemark = operation_mysql().search_one("SELECT remark from `user` ORDER BY created DESC LIMIT 0,1")['remark']
        assert newAgencyRemark == "修改测试代理商备注"
        operation_mysql().close_sql()

    def test_del_agency_rollback(self, drivers):
        '''删除代理商_撤销'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_row()
        agency.click_del()
        agency.swtich_to_default()
        agency.click_cancel()
        newAgencyRemark = operation_mysql().search_one("SELECT remark from `user` ORDER BY created DESC LIMIT 0,1")['remark']
        assert newAgencyRemark == "修改测试代理商备注"
        operation_mysql().close_sql()

    def test_del_agency(self, drivers):
        '''删除代理商'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_row_del()
        agency.swtich_to_default()
        agency.click_confirm()
        agency.click_confirm()
        newAgencyRemark = operation_mysql().search_one("SELECT remark from `user` WHERE flag=0 ORDER BY created DESC LIMIT 0,1")['remark']
        assert newAgencyRemark != "修改测试代理商备注"
        operation_mysql().close_sql()

    def test_disable_agency(self, drivers):
        '''禁用代理商'''
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_enable()
        agency.swtich_to_default()
        agency.click_confirm()
        agency.click_confirm()
        agency.click_quit()
        agency.click_confirm()
        login = LoginPage(drivers)
        login.get_url(conf.url)
        login.input_username('test2')
        login.input_password('123456')
        login.click_login()
        text_agency_disable = login.error_message()
        assert "禁用" in text_agency_disable

    def test_enable_agency(self, drivers):
        '''启用代理商'''
        login = LoginPage(drivers)
        login.get_url(conf.url)
        login.input_username('13800138001')
        login.input_password('123456')
        login.click_login()
        time.sleep(0.5)
        index = Index(drivers)
        index.switch_agency()
        agency = AgencyPage(drivers)
        agency.switch_to_iframe()
        agency.click_enable()
        agency.swtich_to_default()
        agency.click_confirm()
        agency.click_confirm()
        agency.click_quit()
        agency.click_confirm()
        login = LoginPage(drivers)
        login.get_url(conf.url)
        login.input_username('test2')
        login.input_password('123456')
        login.click_login()
        text_agency_enable = login.get_username()
        assert text_agency_enable == 'test2'


# if __name__ == '__main__':
#     pytest.main(['test_agency.py'])








