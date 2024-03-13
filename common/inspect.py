#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import sys
sys.path.append('.')
import os
import yaml
import time
import settings
from Page.basepage import LOCATE_MODE

# if __name__ == '__main__':
def inspect_element():
    """审查所有的元素是否正确"""
    start_time = time.time()
    for i in os.listdir(settings.ELEMENT_PATH):
        _path = os.path.join(settings.ELEMENT_PATH, i)
        if os.path.isfile(_path):
            with open(_path, encoding='utf-8') as f:
                # data = yaml.safe_load(f)
                # print(data, type(data))
                data = yaml.safe_load(f)
                for k in data.values():
                    pattern, value = k['type'], k['value']
                    if pattern not in LOCATE_MODE:
                        raise AttributeError('【%s】路径中【%s]元素没有指定类型' % (i, k))
                    if pattern == 'xpath':
                        assert '//' in value,'【%s】路径中【%s]元素xpath类型与值不配' % (i,k)
                    if pattern == 'css':
                        assert '//' not in value,'【%s】路径中【%s]元素css类型与值不配' % (i, k)
    end_time = time.time()
    print("校验元素done！用时%.3f秒！" % (end_time - start_time))


if __name__ == '__main__':
    inspect_element()
