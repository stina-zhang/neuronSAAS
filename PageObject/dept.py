#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

dept = Element('dept')
class DeptPage(WebPage):
    def click_add(self):
        """点击添加科室"""
        self.is_click(dept.新建)

    def input_dept_name(self,content):
        """输入查询的科室名称"""
        self.input_text(dept.科室名称输入框,content)

    def click_query(self):
        """点击查询"""
        self.is_click(dept.查询)

    def click_reset(self):
        """点击重置"""
        self.is_click(dept.重置)

    def click_save(self):
        """点击保存"""
        self.is_click(dept.保存)

    def click_cancel(self):
        """点击取消"""
        self.is_click(dept.取消)

    def input_new_dept_name(self, content):
        """输入新建的科室名称"""
        self.input_text(dept.新建科室名称输入框, content)

    def select_plat_name(self):
        """选择所属平台"""
        self.is_click(dept.所属平台选择框)
        self.is_click(dept.所属平台选择项)

    def select_tenant_name(self):
        """选择所属机构"""
        self.is_click(dept.所属机构选择框)
        self.is_click(dept.所属机构选择项)

    def select_dept_type(self):
        """选择科室类型"""
        self.is_click(dept.科室类型选择框)
        self.is_click(dept.科室类型选择项)

    def delete_dept(self):
        """删除科室"""
        self.is_click(dept.删除)

    def delete_dept_confirm(self):
        """删除科室"""
        self.is_click(dept.确定删除)

    def get_error_message(self):
        """增加科室提示消息"""
        return self.isElementAttribute(dept.消息提示)

    def get_dept_name(self):
        """增加科室提示消息"""
        return self.isElementText(dept.科室名称)

    def get_dept_status(self):
        """科室状态"""
        return self.isElementText(dept.科室状态)