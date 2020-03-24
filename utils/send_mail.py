#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import os
import zmail
import settings

def send_report():
    """发送报告"""
    with open(settings.REPORT_PATH, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': settings.EMAIL_INFO['username'],  #发件人
            'subject': '多米家SAAS测试报告',  # 邮件标题
            'content_html': content_html,  # 邮件正文
            'attachments': [
                settings.REPORT_PATH,
            ]  # 邮件附件
        }
        server = zmail.server(*settings.EMAIL_INFO.values())
        server.send_mail(settings.ADDRESSEE, mail)
    except Exception as e:
        print("Error: 无法发送邮件:", format(e))
    else:
        print("测试报告邮件发送成功！")

if __name__ == "__main__":
    send_report()