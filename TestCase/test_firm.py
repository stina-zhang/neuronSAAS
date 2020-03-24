#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import pytest
from PageObject.index import Index
from PageObject.firm import FirmPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time
import os

test_add_firm1 = [("","7","test address"),(" ","7","test address"),("test firm","","test address"),("","","test address"),("","7",""),
                  ("test firm","",""),("","",""),("智能厂家智能厂家智能厂家智能厂家智能厂家智","7","test address"),
                  ("test","1000","test address"),("test firm","7","厂家地址厂家地址厂家地址厂家地址厂家地址厂")]
test_add_firm2 = [("测试厂商","7","test address"),("t","7","test address"),("111","7","test address"),("!@#$%^&*()","7","test address"),
                  ("测试厂商测试厂商测试厂商测试厂商测试厂商","7","test address")]
class TestFirm:
    @pytest.fixture(scope='class', autouse=True)
    def open_index_firm(self, drivers, open_loginhtml):
        self.index = Index(drivers)
        self.index.switch_firm()
    #
    @pytest.fixture(scope='function', autouse=False)
    def delete_testfirm(self, drivers):
        yield
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_row()
        firm.click_del()
        firm.swtich_to_default()
        firm.click_confirm()
        firm.click_confirm()
    #
    @pytest.fixture(scope='function', autouse=False)
    def add_testfirm(self, drivers):
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_add()
        firm.input_firm_name("测试厂商")
        firm.input_firm_address("测试厂商测试地址")
        firm.input_firm_code(30)
        firm.click_save()
        firm.swtich_to_default()
        firm.click_confirm()
        firm.click_confirm()

    @pytest.mark.hello
    def test_add_firm_roolback(self, drivers):
        '''新增厂商_撤销'''
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_add()
        firm.input_firm_name("测试厂商1")
        firm.input_firm_code(6)
        firm.input_firm_address("测试厂商测试地址")
        firm.click_rollback()
        firm.swtich_to_default()
        firm.click_confirm()

    # @pytest.mark.hello
    def test_add_firm(self, drivers, delete_testfirm):
        '''新增厂商'''
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_add()
        firm.input_firm_name("测试厂商1")
        firm.input_firm_address("测试厂商测试地址")
        firm.input_firm_code(10)
        firm.click_save()
        firm.swtich_to_default()
        firm.click_confirm()
        firm.click_confirm()

    # @pytest.mark.hello
    @pytest.mark.parametrize("add_firm_name,add_firm_code,add_firm_address",test_add_firm1)
    def test_add_firm_inputerror(self, drivers, add_firm_name, add_firm_code, add_firm_address, expect_message="请输入正确内容"):
        '''新增厂商异常,厂商名称和厂商代码不能为空,名称和地址不超过20个字符，编码不超过1000'''
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_add()
        firm.input_firm_name(add_firm_name)
        firm.input_firm_address(add_firm_address)
        firm.input_firm_code(add_firm_code)
        firm.click_save()
        firm.swtich_to_default()
        time.sleep(0.5)
        firm_error_message = firm.error_message()
        assert expect_message in firm_error_message
        time.sleep(2)
        firm.switch_to_iframe()
        firm.click_rollback()
        firm.switch_default()
        firm.click_confirm()
        time.sleep(1)

    # @pytest.mark.hello
    @pytest.mark.parametrize("add_firm_name,add_firm_code,add_firm_address", test_add_firm2)
    def test_add_firm(self, drivers, add_firm_name, add_firm_code, add_firm_address, delete_testfirm):
        '''新增厂商正常,厂商名称支持特殊字符、中文、英文、数字'''
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_add()
        firm.input_firm_name(add_firm_name)
        firm.input_firm_address(add_firm_address)
        firm.input_firm_code(add_firm_code)
        firm.click_save()
        firm.swtich_to_default()
        firm.click_confirm()
        firm.click_confirm()
        new_firm_name = operation_mysql().search_one("SELECT * FROM firm WHERE flag=0 ORDER BY created DESC LIMIT 0,1")["name"]
        assert add_firm_name == new_firm_name

    # @pytest.mark.hello
    def test_edit_firm(self, drivers, add_testfirm, delete_testfirm):
        '''修改厂商名称、地址'''
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_row()
        firm.click_edit()
        firm.input_firm_name("修改测试厂商1")
        firm.input_firm_address("修改测试厂商地址1")
        firm.click_save()
        firm.swtich_to_default()
        firm.click_confirm()
        firm.click_confirm()
        firm_edit_name = operation_mysql().search_one(sql="SELECT * FROM firm WHERE flag=0 ORDER BY created DESC LIMIT 0,1")['name']
        assert firm_edit_name == '修改测试厂商1'

    # @pytest.mark.hello
    def test_del_firm(self, drivers, add_testfirm):
        '''删除厂商'''
        firm = FirmPage(drivers)
        firm.switch_to_iframe()
        firm.click_row()
        firm.click_del()
        firm.swtich_to_default()
        firm.click_cancel()
        firm.switch_to_iframe()
        firm.click_row()
        firm.click_del()
        firm.swtich_to_default()
        firm.click_confirm()
        firm.click_confirm()
        firm_number = operation_mysql().search_all(sql="SELECT * FROM firm WHERE flag=0")[0]
        assert firm_number == 5



if __name__ == '__main__':
    pytest.main(['test_firm.py', '-m=hello', '--maxfail=10', '--alluredir=./allure_results'])
    os.system('allure generate ./allure_results/ -o ./allure_reports --clean')