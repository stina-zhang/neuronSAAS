#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

role = Element('role')
class RolePage(WebPage):

    def click_add(self):
        """点击添加角色"""
        self.is_click(role.增加)

    def click_edit(self):
        """点击修改角色"""
        self.is_click(role.修改)

    def click_del(self):
        """点击删除角色"""
        self.is_click(role.删除)

    def input_role_name(self, content):
        """输入角色名称"""
        self.input_text(role.名称输入框, content)

    def input_role_remark(self, content):
        """输入角色备注"""
        self.input_text(role.备注输入框, content)

    def input_role_code(self, content):
        """输入角色编码"""
        self.input_text(role.编码输入框, content)

    def click_role_permission(self):
        """点击角色权限"""
        self.is_click(role.权限选择框)

    def click_select_all(self):
        """选择角色所有权限"""
        self.is_click(role.全选)

    def click_select_first(self):
        """选择角色第一行"""
        self.is_click(role.权限第一行)

    def click_select_tenth(self):
        """选择角色第十行"""
        self.is_click(role.权限第十行)

    def click_last_row(self):
        """选择最后一行"""
        self.is_click(role.最后一行)

    def click_save(self):
        """保存"""
        self.is_click(role.保存)

    def click_rollback(self):
        """撤销"""
        self.is_click(role.撤销)

    def click_confirm(self):
        """确定"""
        self.is_click(role.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(role.取消)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)