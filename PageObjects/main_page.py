#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from test.automation_app.PO.Common.base_log import logger
from test.automation_app.PO.Common.base_page import BasePage
from test.automation_app.PO.PageObjects.safetyProtection_page import SafetyProtectionPage


class MainPage(BasePage):
    _SafetyProtection_locator = (
        By.XPATH, "//*[@resource-id='com.sensoro.lingsi:id/rv_app_list']/android.widget.LinearLayout[1]"
    )

    def to_SafetyProtection(self):
        # 进入安全防护页面
        self.find_element_click(self._SafetyProtection_locator)
        return SafetyProtectionPage(self.driver)
