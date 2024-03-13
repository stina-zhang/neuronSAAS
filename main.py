#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
import sys
import os
import shutil
sys.path.append('.')

if __name__ == '__main__':
    pytest.main()
    shutil.copy('./environment.properties', './allure_results')
    os.system('allure generate ./allure_results -o ./allure_reports --clean')
