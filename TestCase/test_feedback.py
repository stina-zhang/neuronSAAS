#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import pytest
from PageObject.loginpage import LoginPage
from PageObject.index import Index
from PageObject.feedbackpage import FeedbackPage
from common.readconfig import conf
from common.connect_db import operation_mysql
import time
import random

class TestFeedback:
    @pytest.fixture(scope='class', autouse=True)
    def open_loginhtml(self, drivers):
        self.login = LoginPage(drivers)
        self.login.get_url(conf.url)
        self.login.input_username('13800138001')
        self.login.input_password('123456')
        self.login.click_login()
        time.sleep(0.5)
        self.index = Index(drivers)
        self.index.switch_feedback()

    def test_add_feedback(self, drivers):
        '''新增反馈'''
        feedback = FeedbackPage(drivers)
        feedback.switch_to_iframe()
        # feedback.click_last_row()
        feedback.click_feedback()
        feedback.swtich_to_default()
        feedback_content = "平台回复"+str(random.randint(1,100))
        feedback.input_feedback(feedback_content)
        feedback.click_confirm()
        feedback.click_confirm()
        feedback.switch_to_iframe()
        new_feedback_content = feedback.feedback_text()
        assert feedback_content == new_feedback_content

if __name__ == '__main__':
    pytest.main(['test_feedback.py'])