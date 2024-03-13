#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
from Page.basepage import WebPage, sleep
from common.readelement import Element

feedback = Element('feedback')
class FeedbackPage(WebPage):

    def input_feedback(self, content):
        """输入回复内容"""
        self.input_text(feedback.回复输入框, content)

    def click_feedback(self):
        """点击回复"""
        self.is_click(feedback.回复)

    def click_del(self):
        """点击删除"""
        self.is_click(feedback.删除)

    def click_last_row(self):
        """选择最后一行"""
        self.is_click(feedback.最后一行)

    def click_confirm(self):
        """确定"""
        self.is_click(feedback.确定)

    def click_cancel(self):
        """取消"""
        self.is_click(feedback.取消)

    def switch_iframe(self):
        """切换到iframe页面"""
        self.switch_to_iframe()
        sleep(1)

    def switch_default(self):
        """切换到主页面"""
        self.swtich_to_default()
        sleep(1)

    def feedback_text(self):
        """获取回复内容"""
        return self.isElementText(feedback.回复内容)
