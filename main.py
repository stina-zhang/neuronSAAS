#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
sys.path.append('.')
import pytest


if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./allure_results -o ./allure_reports --clean')