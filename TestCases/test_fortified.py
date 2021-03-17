#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from test.automation_app.PO.Common.base_driver import Android_app


class Test:
    def setup(self):
        self.safetyProtection_page = Android_app.start('lins_android.yaml').to_SafetyProtection()

    def test_all_fortified_po(self):
        '''左右滑动切换任务，并进行全部设防/全部撤防操作'''
        self.safetyProtection_page.switch_task_left(3)
        self.safetyProtection_page.switch_task_right(3)
        self.safetyProtection_page.all_fortified_area()
        assert self.safetyProtection_page.is_toast_exist("全部设防成功！") == True
        time.sleep(3)
        self.safetyProtection_page.all_removal_area()
        assert self.safetyProtection_page.is_toast_exist("全部撤防成功！") == True
        time.sleep(2)

    def teardown(self):
        Android_app.quit()
