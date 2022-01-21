#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs','TestCases/', '--alluredir', './Temp'])
    os.system('allure generate ./Temp -o ./TestReport --clean')