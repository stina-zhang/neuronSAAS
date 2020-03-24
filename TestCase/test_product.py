#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from PageObject.productpage import ProductPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time

class TestProduct:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(0.5)
        self.index = Index(drivers)
        self.index.switch_product()

    def test_add_product_roolback(self, drivers):
        '''新增产品_撤销'''
        product = ProductPage(drivers)
        product.switch_to_iframe()
        product.click_add()
        product.input_product_name("测试产品")
        product.input_product_code(600)
        product.click_select_ability()
        product.click_select_ability_all()
        product.click_select_ability()
        product.click_select_firm()
        time.sleep(0.5)
        product.click_select_firm_test()
        time.sleep(0.5)
        product.click_select_ability()
        product.click_select_ability_all()
        product.click_select_ability()
        product.click_rollback()
        product.swtich_to_default()
        product.click_confirm()
        product_add_name = operation_mysql().search_one(sql="SELECT * from product WHERE flag=0 ORDER BY created DESC LIMIT 0,1")[
            'name']
        assert product_add_name != "测试产品"

    def test_add_product(self, drivers):
        '''新增产品'''
        product = ProductPage(drivers)
        product.switch_to_iframe()
        product.click_add()
        product.input_product_name("测试产品")
        product.input_product_code(600)
        product.click_select_firm()
        time.sleep(0.5)
        product.click_select_firm_test()
        product.click_select_ability()
        product.click_select_ability_all()
        product.click_select_ability()
        product.click_save()
        product.swtich_to_default()
        product.click_confirm()
        product.click_confirm()
        product_add_name = operation_mysql().search_one(sql="SELECT * from product WHERE flag=0 ORDER BY created DESC LIMIT 0,1")['name']
        assert product_add_name == "测试产品"

    def test_edit_product(self, drivers):
        '''修改产品'''
        product = ProductPage(drivers)
        product.switch_to_iframe()
        product.click_last_row()
        product.click_edit()
        product.input_product_name("修改测试产品")
        product.input_product_code(601)
        product.click_save()
        product.swtich_to_default()
        product.click_confirm()
        product.click_confirm()
        product_add_name = operation_mysql().search_one(sql="SELECT * from product WHERE flag=0 ORDER BY created DESC LIMIT 0,1")['name']
        assert product_add_name == "修改测试产品"


    def test_del_product_rollback(self, drivers):
        '''删除产品'''
        product = ProductPage(drivers)
        product.switch_to_iframe()
        product.click_last_row()
        product.click_del()
        product.swtich_to_default()
        product.click_cancel()
        product_add_name = operation_mysql().search_one(sql="SELECT * from product WHERE flag=0 ORDER BY created DESC LIMIT 0,1")[
            'name']
        assert product_add_name == "修改测试产品"

    def test_del_product(self, drivers):
        '''删除产品'''
        product = ProductPage(drivers)
        product.switch_to_iframe()
        product.click_last_row()
        product.click_del()
        product.swtich_to_default()
        product.click_confirm()
        product.click_confirm()
        product_add_name = operation_mysql().search_one(sql="SELECT * from product WHERE flag=0 ORDER BY created DESC LIMIT 0,1")[
            'name']
        assert product_add_name != "修改测试产品"

# if __name__ == '__main__':
#     pytest.main(['test_product.py'])
