#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys,os
sys.path.append('.')
import pytest
from PageObject.index import Index
import time
import allure

@pytest.mark.run(order=1)
@allure.feature("首页切换测试")
class TestIndex:
    @allure.story("切换到类型管理机构类型管理页面")
    def test_switch_typeManage(self, drivers):
        '''切换到类型管理机构类型管理页面'''
        index = Index(drivers)
        index.switch_typeManage()
        index.switch_tenentTypeManage()
        assert "机构类型名称" in index.get_text_tenentTypeName()
        time.sleep(1)

    @allure.story("切换到运营管理机构管理页面")
    def test_switch_staticeManage(self, drivers):
        '''切换到运营管理机构管理页面'''
        index = Index(drivers)
        index.switch_operationMange()
        index.switch_tenantMange()
        time.sleep(1)
        assert "机构列表" in index.get_text_tenantList()
        time.sleep(1)

    @allure.story("切换到系统管理平台管理页面")
    def test_switch_systemManage(self, drivers):
        '''切换到系统管理平台管理页面'''
        index = Index(drivers)
        index.switch_systemManage()
        index.switch_platMange()
        time.sleep(1)
        assert "平台编号" in index.get_text_platNumber()
        time.sleep(1)

    @allure.story("切换到统计机构检查数据页面")
    def test_switch_statics(self, drivers):
        '''切换到统计机构检查数据页面'''
        index = Index(drivers)
        index.switch_statics()
        index.switch_tenantCheckData()
        assert "机构检查数据统计" in index.get_text_statice()
        time.sleep(1)

    # @allure.story("切换到科室管理页面")
    # def test_switch_deptManage(self, drivers):
    #     '''切换到科室管理页面'''
    #     index = Index(drivers)
    #     index.switch_operationMange()
    #     index.switch_deptMange()
    #     assert "科室名称" in index.get_text_deptName()
    #     time.sleep(1)



