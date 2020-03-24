#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from utils.log import log
import time
from common.readconfig import conf
"""
selenium基类
本文件存放了selenium基类的封装方法
"""

# 元素定位类型
LOCATE_MODE = {
    'id': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'class_name': By.CLASS_NAME,
    'css': By.CSS_SELECTOR
}


def sleep(seconds=1.0):
    '''
    等待时间
    :return 有些提示框不强制等待，只用显式等待会导致执行报错
    '''
    time.sleep(seconds)


class WebPage:
    """selenium基类"""
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        '''打开网址并验证'''
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def selector(func, locator):
        pattern, value = locator['type'], locator['value']
        return func(LOCATE_MODE[pattern], value)

    def findelement(self, locator):
        """寻找单个元素"""
        function = lambda *args: self.wait.until(lambda x: x.find_element(*args
                                                                          ))
        return WebPage.selector(function, locator)

    def findelements(self, locator):
        '''查找多个相同的元素'''
        functions = lambda *args: self.wait.until(lambda x: x.find_elements(
            *args))
        return WebPage.selector(functions, locator)

    def isElementNum(self, locator):  # 获取相同元素的个数
        '''获取相同元素的个数'''
        number = len(self.findelements(locator))
        return number

    def is_clear(self, locator):
        '''清空输入框'''
        self.findelement(locator).clear()
        self.driver.implicitly_wait(0.5)

    def input_text(self, locator, txt):
        '''输入(输入前先清空)'''
        self.findelement(locator).clear()
        self.driver.implicitly_wait(0.5)
        self.findelement(locator).send_keys(txt)
        self.driver.implicitly_wait(0.5)
        log.info("在元素%s中输入%s" % (locator, txt))

    def input_text_no_clear(self, locator, txt):
        '''输入'''
        self.findelement(locator).send_keys(txt)
        self.driver.implicitly_wait(0.5)
        log.info("在元素%s中输入%s" % (locator, txt))

    def is_click(self, locator):
        '''点击'''
        function = lambda *args: self.wait.until(EC.element_to_be_clickable(args))
        ele = WebPage.selector(function, locator)
        ele.click()
        log.info("点击元素%s" % locator)
        self.driver.implicitly_wait(0.5)

    def double_click(self, locator):
        '''双击'''
        ele = self.findelement(locator)
        self.driver.implicitly_wait(0.5)
        ActionChains(self.driver).double_click(ele).perform()
        log.info("双击元素%s" % locator)
        self.driver.implicitly_wait(0.5)

    def switch_to_iframe(self):
        '''切换到iframe'''
        sleep(0.5)
        self.driver.switch_to.frame('mainiframe')
        self.driver.implicitly_wait(0.5)
        log.info("切换iframe")

    def isElementText(self, locator):
        '''获取当前的text'''
        return self.findelement(locator).text

    @property
    def getSource(self):
        """获取页面源代码"""
        return self.driver.page_source

    def getTitle(self):
        """获取页面标题"""
        return self.driver.title

    def getAlertText(self):
        """获取页面标题"""
        return self.driver.switch_to.alert().text

    def shot_file(self, path):
        '''文件截图'''
        return self.driver.save_screenshot(path)

    def close(self):
        '''关闭当前标签'''
        self.driver.close()

    def swtich_to_default(self):
        '''切换到默认标签'''
        self.driver.switch_to.default_content()

    def refresh(self):
        '''刷新页面F5'''
        self.driver.refresh()
        self.driver.implicitly_wait(30)


# if __name__ == "__main__":
#     pass
