#!/usr/bin/python
# -*- coding:utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from test.automation_app.PO.Common.base_log import logger


def handle_except(func):
    def wrapper(*args, **kwargs):
        from test.automation_app.PO.Common.base_page import BasePage
        _black_list = [
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, '//*[@text="下次再说"]'),
            (By.XPATH, '//*[@text="确定"]')
        ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]

        try:
            logger.info("run" + func.__name__ + "\n args:\n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            # 隐式等待恢复原来的等待
            instance.driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 如果有异常就截图
            instance.screenshots()
            logger.error("element not found,handle except list")
            instance.driver.implicitly_wait(1)
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance.driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹窗，再去查找目标元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
