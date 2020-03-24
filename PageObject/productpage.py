#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

product = Element('product')
class ProductPage(WebPage):

    def click_add(self):
        """点击添加产品"""
        self.is_click(product.增加)

    def click_edit(self):
        """点击修改产品"""
        self.is_click(product.修改)

    def click_del(self):
        """点击删除产品"""
        self.is_click(product.删除)

    def input_product_name(self, content):
        """输入产品名称"""
        self.input_text(product.名称输入框, content)

    def input_product_code(self, content):
        """输入产品编码"""
        self.input_text(product.编码输入框, content)

    def click_select_firm(self):
        """点击选择厂商复选框"""
        self.is_click(product.厂商名称复选框)

    def click_select_firm_test(self):
        """点击选择测试厂商"""
        self.is_click(product.厂商选择)

    def click_select_ability(self):
        """点击选择产品能力复选框"""
        self.is_click(product.产品能力复选框)

    def click_select_ability_all(self):
        """点击选择产品能力复选框"""
        self.is_click(product.全选)

    def click_last_row(self):
        """选择最后一行"""
        self.is_click(product.最后一行)

    def click_save(self):
        """保存"""
        self.is_click(product.保存)

    def click_rollback(self):
        """撤销"""
        self.is_click(product.撤销)

    def click_confirm(self):
        """确定"""
        self.is_click(product.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(product.取消)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)