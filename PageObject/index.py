#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element


index = Element('index')
class Index(WebPage):

    def switch_index(self):
        """切换到首页"""
        self.is_click(index.首页)
        sleep(1)

    def switch_device(self):
        """切换到设备管理页面"""
        self.is_click(index.设备管理)
        sleep(1)

    def switch_message(self):
        """切换到消息列表页面"""
        self.is_click(index.消息列表)
        sleep(1)

    def switch_feedback(self):
        """切换到反馈信息页面"""
        self.is_click(index.反馈信息)
        sleep(1)

    def switch_product(self):
        """切换到产品管理页面"""
        self.is_click(index.产品管理)
        sleep(1)

    def switch_product_ability(self):
        """切换到产品能力管理页面"""
        self.is_click(index.产品能力管理)
        sleep(1)

    def switch_firm(self):
        """切换到厂商管理页面"""
        self.is_click(index.厂商管理)
        sleep(1)

    def switch_agency(self):
        """切换到代理商管理页面"""
        self.is_click(index.代理商管理)
        sleep(1)

    def switch_role(self):
        """切换到角色管理页面"""
        self.is_click(index.角色管理)
        sleep(1)

    def switch_peimission(self):
        """切换到权限管理页面"""
        self.is_click(index.权限管理)
        sleep(1)

    def switch_account(self):
        """切换到账号管理页面"""
        self.is_click(index.账号管理)
        sleep(1)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)

    def ifram_text(self):
        return self.isElementText(index.ifram标题)

    def get_device_total(self):
        return self.isElementText(index.设备总量)

    def get_device_online(self):
        return self.isElementText(index.设备在线量)

    def get_device_offline(self):
        return self.isElementText(index.设备离线量)

    def get_device_alarm(self):
        return self.isElementText(index.设备异常量)

    def get_device_inc_day(self):
        return self.isElementText(index.设备日增量)

    def get_device_act_day(self):
        return self.isElementText(index.设备日活跃量)

    def get_device_act_total(self):
        return self.isElementText(index.设备活跃总量)

    def get_user_inc_day(self):
        return self.isElementText(index.用户日增量)

    def get_user_act_day(self):
        return self.isElementText(index.用户日活跃量)

    def get_user_act_total(self):
        return self.isElementText(index.用户活跃总量)