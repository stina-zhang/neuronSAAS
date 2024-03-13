#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
sys.path.append('.')

import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 配置文件
CONFIG_PATH = os.path.join(BASE_DIR, 'config.ini')
# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'PageElements')
# SQLite数据库
SQLITE_PATH = os.path.join(BASE_DIR, 'TestData', 'sqlite3.sqlite')
# 截图目录
SCREENSHOT_PATH = os.path.join(BASE_DIR, 'screenshot')
# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'logs')
# 报告文件
REPORT_PATH = os.path.join(BASE_DIR, '')
# 邮件信息
EMAIL_INFO = {
    'username': 'yuhe587853@163.com',
    'password': 'MBBHPIKRSQOOEBXS',
    'smtp_host': 'smtp.163.com',
    # 'smtp_port': 465
}
# 收件人
ADDRESSEE = [
    '1055607469@qq.com',
]

# if __name__ == '__main__':
#     print(BASE_DIR)
#     print(ELEMENT_PATH)