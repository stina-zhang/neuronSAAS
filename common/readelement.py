#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import os
import yaml
import settings


class Element:
    """获取元素"""
    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(settings.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getattr__(self, item):
        sections = self.data.get(item)
        if sections:
            return sections
        else:
            raise AttributeError("文件%s关键字【%s】获取元素结果为空" %
                                 (self.file_name, item))


