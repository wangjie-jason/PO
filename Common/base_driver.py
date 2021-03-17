#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from test.automation_app.PO.PageObjects.main_page import MainPage


class Android_app:
    driver: WebDriver

    @classmethod
    def start(cls, app_filecfg):
        # 获取初始化配置数据
        path = os.path.dirname(os.path.abspath(__file__))
        a_path = os.path.abspath(os.path.join(path, '../Testcfg'))
        print(a_path)

        with open(a_path + '/' + app_filecfg, 'r') as file:
            cls.data = yaml.safe_load(file)
            print(cls.data)

        # 传入初始化启动参数
        caps = {}
        caps["platformName"] = cls.data["platformName"]
        caps["appPackage"] = cls.data["appPackage"]
        caps["appActivity"] = cls.data["appActivity"]
        caps["autoGrantPermissions"] = cls.data["autoGrantPermissions"]
        udid = os.getenv('UDID', None)
        if udid != None:
            caps["udid"] = udid
            print("udid=%s" % udid)
        caps["noReset"] = cls.data["noReset"]
        caps["ensureWebviewsHavePages"] = cls.data["ensureWebviewsHavePages"]
        caps["unicodeKeyboart"] = cls.data["unicodeKeyboart"]
        print(caps)
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        time.sleep(2)
        cls.driver.quit()
