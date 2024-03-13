#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element


firm = Element('firm')
class FirmPage(WebPage):

    def click_add(self):
        """点击添加厂商"""
        self.is_click(firm.增加)


    def click_edit(self):
        """点击修改厂商"""
        self.is_click(firm.修改)


    def click_del(self):
        """点击删除厂商"""
        self.is_click(firm.删除)


    def input_firm_name(self, content):
        """输入厂商名称"""
        self.input_text(firm.厂商名称输入框, content)


    def input_firm_code(self, content):
        """输入厂商编码"""
        self.input_text(firm.编码输入框, content)


    def input_firm_address(self, content):
        """输入厂商地址"""
        self.input_text(firm.地址输入框, content)


    def click_save(self):
        """保存"""
        self.is_click(firm.保存)


    def click_rollback(self):
        """撤销"""
        self.is_click(firm.撤销)


    def click_confirm(self):
        """确定"""
        self.is_click(firm.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(firm.取消)

    def click_row(self):
        """选择最后一行"""
        self.is_click(firm.选择最后一行)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)

    def ifram_text(self):
        return self.isElementText(firm.ifram标题)

    def error_message(self):
        return self.isElementText(firm.出错提示)

    def last_row_firmname(self):
        return self.isElementText(firm.最后一行厂商名称)









