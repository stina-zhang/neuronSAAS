#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

agency = Element('agency')
class AgencyPage(WebPage):

    def click_add(self):
        """点击添加代理商"""
        self.is_click(agency.增加)

    def click_edit(self):
        """点击修改代理商"""
        self.is_click(agency.修改)

    def click_del(self):
        """点击删除代理商"""
        self.is_click(agency.删除)

    def input_agency_name(self, content):
        """输入代理商名称"""
        self.input_text(agency.代理商名称输入框, content)

    def input_agency_remark(self, content):
        """输入代理商备注"""
        self.input_text(agency.备注输入框, content)

    def click_save(self):
        """保存"""
        self.is_click(agency.保存)

    def click_rollback(self):
        """撤销"""
        self.is_click(agency.撤销)

    def click_row_del(self):
        """删除行"""
        self.is_click(agency.删除行)

    def click_enable(self):
        """禁用"""
        self.is_click(agency.禁用)

    def click_confirm(self):
        """确定"""
        self.is_click(agency.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(agency.取消)

    def click_row(self):
        """选择最后一行"""
        self.is_click(agency.选择最后一行)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)

    def ifram_text(self):
        return self.isElementText(agency.ifram标题)

    def click_quit(self):
        """退出页面"""
        self.is_click(agency.退出)

