#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element


index = Element('index')
class Index(WebPage):

    def switch_systemManage(self):
        """切换到系统管理页面"""
        self.is_click(index.系统管理)
        sleep(1)

    def switch_platMange(self):
        """切换到平台管理页面"""
        self.is_click(index.平台管理)
        sleep(1)

    def get_text_platManage(self):
        return self.isElementText(index.平台管理文本)

    def get_text_tenent(self):
        return self.isElementText(index.所属机构)

    def get_text_user(self):
        return self.isElementText(index.用户名)

    def get_text_platNumber(self):
        return self.isElementText(index.平台编号)

    def switch_roleMange(self):
        """切换到角色管理页面"""
        self.is_click(index.角色管理)
        sleep(1)

    def get_text_roleName(self):
        self.isElementText(index.角色名称)

    def switch_accoutMange(self):
        """切换到账号管理页面"""
        self.is_click(index.账号管理)
        sleep(1)

    def get_text_accoutName(self):
        self.isElementText(index.账号名称)

    def switch_operationMange(self):
        """切换到运营管理页面"""
        self.is_click(index.运营管理)
        sleep(1)

    def switch_tenantMange(self):
        """切换到机构管理页面"""
        self.is_click(index.机构管理)
        sleep(1)

    def get_text_tenantList(self):
        return self.isElementText(index.机构列表)

    def switch_deptMange(self):
        """切换到科室管理管理页面"""
        self.is_click(index.科室管理)
        sleep(1)

    def get_text_deptName(self):
        return self.isElementText(index.科室名称)

    def switch_doctorMange(self):
        """切换到医生管理页面"""
        self.is_click(index.医生管理)
        sleep(1)

    def switch_doctorRoleManage(self):
        """切换到医生角色管理页面"""
        self.is_click(index.医生角色管理)
        sleep(1)

    def get_text_doctorRoleName(self):
        return self.isElementText(index.医生角色名称)

    def switch_doctorAccoutManage(self):
        """切换到医生账号管理页面"""
        self.is_click(index.医生账号管理)
        sleep(1)

    def get_text_doctorAccoutName(self):
        return self.isElementText(index.医生账号名称)

    def switch_patientManage(self):
        """切换到患者管理页面"""
        self.is_click(index.患者管理)
        sleep(1)

    def get_text_name(self):
        return self.isElementText(index.姓名)

    def switch_deviceManage(self):
        """切换到设备管理页面"""
        self.is_click(index.设备管理)
        sleep(1)

    def get_text_deviceType(self):
        return self.isElementText(index.设备类型)

    def switch_typeManage(self):
        """切换到类型管理页面"""
        self.is_click(index.类型管理)
        sleep(1)

    def switch_tenentTypeManage(self):
        """切换到机构类型管理页面"""
        self.is_click(index.机构类型管理)
        sleep(1)

    def get_text_tenentTypeName(self):
        return self.isElementText(index.机构类型名称)

    def switch_deptTypeManage(self):
        """切换到科室类型管理页面"""
        self.is_click(index.科室类型管理)
        sleep(1)

    def get_text_deptTypeName(self):
        return self.isElementText(index.科室类型名称)

    def switch_doctorRoleTypeManage(self):
        """切换到医生角色类型管理页面"""
        self.is_click(index.医生角色类型管理)
        sleep(1)

    def get_text_doctorRoleTypeName(self):
        return self.isElementText(index.医生角色类型名称)

    def switch_deviceTypeManage(self):
        """切换到设备类型管理页面"""
        self.is_click(index.设备类型管理)
        sleep(1)

    def get_text_deviceTypeName(self):
        return self.isElementText(index.设备类型名称)

    def switch_statics(self):
        """切换到统计页面"""
        self.is_click(index.统计)
        sleep(1)

    def switch_tenantCheckData(self):
        """切换到机构检查数据页面"""
        self.is_click(index.机构检查数据)
        sleep(1)

    def get_text_statice(self):
        return self.isElementText(index.统计文本)

    def switch_tenantAnalysitData(self):
        """切换到机构分析数据页面"""
        self.is_click(index.机构分析数据)
        sleep(1)

    def switch_doctorWork(self):
        """切换到医生工作量页面"""
        self.is_click(index.医生工作量)
        sleep(1)

    def switch_express(self):
        """切换到物流运单页面"""
        self.is_click(index.物流运单)
        sleep(1)
