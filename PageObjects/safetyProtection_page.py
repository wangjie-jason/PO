#!/usr/bin/python
# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By

from test.automation_app.PO.Common.base_page import BasePage


class SafetyProtectionPage(BasePage):
    # 向左滑动切换安全防护任务
    def switch_task_left(self, n):
        for i in range(n):
            if n == 1:
                _a = (By.XPATH, "//*[@resource-id='com.sensoro.lingsi:id/rv_task']/android.view.ViewGroup")
                b = self.find_element(_a)
            else:
                _a = (By.XPATH, "//*[@resource-id='com.sensoro.lingsi:id/rv_task']/android.view.ViewGroup[2]")
                b = self.find_element(_a)
            self.swipe_to_left(text_element=b)
        return self

    # 向右滑动切换安全防护任务
    def switch_task_right(self, n):
        for i in range(n):
            _a = (By.XPATH, "//*[@resource-id='com.sensoro.lingsi:id/rv_task']/android.view.ViewGroup[2]")
            b = self.find_element(_a)
            self.swipe_to_right(text_element=b)
        return self

    _all_switch_on = (By.ID, 'com.sensoro.lingsi:id/ll_all_switch_on')
    _confirm_button = (By.ID, 'com.sensoro.lingsi:id/tv_confirm')

    # 对区域进行全部设防
    def all_fortified_area(self):
        self.find_element_click(self._all_switch_on)
        self.find_element_click(self._confirm_button)
        return self

    _all_switch_off = (By.ID, 'com.sensoro.lingsi:id/ll_all_switch_off')

    # 对区域进行全部撤防
    def all_removal_area(self):
        self.find_element_click(self._all_switch_off)
        self.find_element_click(self._confirm_button)
        return self
