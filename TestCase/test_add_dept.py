#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
import random
import pytest
from PageObject.index import Index
from PageObject.dept import DeptPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time,os,allure


@pytest.mark.run(order=2)
@allure.feature("科室管理测试")
class TestDept:
    @pytest.fixture(scope='class', autouse=True)
    def switch_dept_manage(self, drivers):
        index = Index(drivers)
        index.switch_operationMange()
        index.switch_deptMange()

    @allure.story("增加科室，未输入机构名称")
    def test_add_dept_noTenantName(self, drivers):
        dept = DeptPage(drivers)
        dept.click_add()
        time.sleep(1)
        dept.input_new_dept_name("test_deptname")
        dept.select_plat_name()
        # dept.select_tenant_name()
        dept.select_dept_type()
        dept.click_save()
        message = dept.get_error_message()
        assert "不能为空" in message
        dept.click_cancel()
    #
    @allure.story("增加科室，未输入平台名称")
    def test_add_dept_noPlatName(self, drivers):
        dept = DeptPage(drivers)
        dept.click_add()
        time.sleep(1)
        dept.input_new_dept_name("test_deptname")
        # dept.select_plat_name()
        dept.select_tenant_name()
        dept.select_dept_type()
        dept.click_save()
        message = dept.get_error_message()
        assert "不能为空" in message
        dept.click_cancel()
    #
    @allure.story("增加科室，未输入类型名称")
    def test_add_dept_noDeptType(self, drivers):
        dept = DeptPage(drivers)
        dept.click_add()
        time.sleep(1)
        dept.input_new_dept_name("test_deptname")
        dept.select_plat_name()
        dept.select_tenant_name()
        # dept.select_dept_type()
        dept.click_save()
        message = dept.get_error_message()
        assert "不能为空" in message
        dept.click_cancel()
    @allure.story("增加科室，输入所有参数")
    def test_add_dept(self, drivers):
        deptname = "test_deptname"+str(random.randint(10,99))
        dept = DeptPage(drivers)
        dept.click_add()
        time.sleep(1)
        dept.input_new_dept_name(deptname)
        dept.select_plat_name()
        dept.select_tenant_name()
        dept.select_dept_type()
        dept.click_save()
        time.sleep(2)
        print(dept.get_dept_name())
        assert dept.get_dept_name() == deptname
    @allure.story("删除科室")
    def test_delete_dept(self, drivers):
        dept = DeptPage(drivers)
        print(dept.get_dept_status())
        dept.delete_dept()
        dept.delete_dept_confirm()
        time.sleep(2)
        dept_status = dept.get_dept_status()
        assert dept_status == "失效"








