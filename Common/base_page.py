#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test.automation_app.PO.Common.base_log import logger


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 截图
    def screenshots(self):
        '''
        截图
        :return: None
        '''
        date_time = time.strftime('%Y-%m-%d %H:%M:%S')
        screenshot_name = 'Manual_' + date_time + '.PNG'
        output_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../TestReport'))
        path = os.path.join(output_path, screenshot_name)
        logger.info(f'screen shot saved in {path}')
        self.driver.get_screenshot_as_file(path)
        # 将图片插入allure中
        with open(path, "rb") as f:
            content = f.read()
        allure.attach(content, attachment_type=allure.attachment_type.PNG)

    # 查找元素
    def find_element(self, locator, timeout=20):
        '''
        查找元素
        :param locator: 定位的方式及需要定位的元素，以元组方式传入
        :param timeout:查找元素超时时间
        :return:返回可见元素
        '''
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator)
            )
        # return self.driver.find_element(*locator)
        except Exception as e:
            self.screenshots()
            logger.error('获取可视化元素失败：{}'.format(e))

    # 查找元素并点击
    def find_element_click(self, locator, timeout=20):
        '''
        查找元素并点击
        :param locator: 定位的方式及需要定位的元素，以元组方式传入
        :param timeout:查找元素超时时间
        :return:返回可点击元素并点击
        '''
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.element_to_be_clickable(locator)
            ).click()
        except Exception as e:
            self.screenshots()
            logger.error('获取可点击元素失败：{}'.format(e))
        # return self.driver.find_element(*locator).click()

    # 查找元素并输入
    def find_element_send_keys(self, locator, value, timeout=20, ):
        '''
        查找元素并输入
        :param locator: 定位的方式及需要定位的元素，以元组方式传入
        :param value: 需要输入的文本内容，传入字符串
        :param timeout: 查找元素超时时间
        :return: 返回存在元素并输入内容
        '''
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located(locator)
            ).send_keys(value)
        except Exception as e:
            self.screenshots()
            logger.error('获取存在元素失败：{}'.format(e))
        # return self.driver.find_element(*locator).send_keys(value)

    # 判断toast是否存在
    def is_toast_exist(self, toastmessage, timeout=20, poll_frequency=0.1):
        '''
        判断toast是否存在
        :param toastmessage: toast的文本内容
        :param timeout:查找元素超时时间
        :param poll_frequency:查找频率时间
        :return:布尔值
        '''
        try:
            toast_loc = (By.XPATH, "//*[contains(@text,'%s')]" % toastmessage)
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                expected_conditions.presence_of_element_located(toast_loc)
            )
            logger.info(self.driver.find_element(*toast_loc).text)
            return True
        except Exception as e:
            logger.error('Toast not found: {}'.format(e))
            return False

    # 滑动页面并通过text属性查找元素
    def swipe_find_element_for_text(self, text):
        '''
        滑动页面并通过text属性查找元素
        :param text: 元素的text属性
        :return: 返回查该元素
        '''
        try:
            return self.driver.find_element_by_android_uiautomator(
                f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));'
            )
        except Exception as e:
            self.screenshots()
            logger.error('滑动查找元素失败：{}'.format(e))

    # 获取手机屏幕分辨率
    def get_window_size(self):
        '''获取手机屏幕分辨率'''
        try:
            return self.driver.get_window_size()
        except Exception as e:
            logger.error('获取手机屏幕分辨率失败：{}'.format(e))

    @property
    # 获取屏幕的宽度
    def _width(self):
        return self.get_window_size()['width']

    @property
    # 获取屏幕的高度
    def _height(self):
        return self.get_window_size()['height']

    # 获取元素的各坐标点
    def _get_element_size(self, text_element):
        '''
        获取元素的各坐标点
        :param text_element: 需要获取坐标的控件
        :return: 元素各坐标点
        '''
        el_width = text_element.size['width']
        el_height = text_element.size['height']
        x = text_element.location['x']
        y = text_element.location['y']

        x_left = x
        x_right = x + el_width
        y_top = y
        y_down = y + el_height
        x_center = (x_left + x_right) / 2
        y_center = (y_top + y_down) / 2
        return x_left, x_right, y_top, y_down, x_center, y_center

    # 从下向上滑动
    def swipe_to_up(self, n=1, base=0.1, duration=1000, text_element=None):
        '''
        从下向上滑动
        :param n: 滑动次数，默认为1
        :param base:辅助参数，忽略
        :param duration:滑动持续时间
        :param text_element:需要滑动的控件
        :return:None
        '''
        try:
            for i in range(n):
                if text_element != None:
                    x_left, x_right, y_top, y_down, x_center, y_center = self._get_element_size(text_element)
                    self.driver.swipe(x_center,
                                      y_down * (1 - base),
                                      x_center,
                                      y_down * base,
                                      duration
                                      )
                else:
                    self.driver.swipe(self._width * 0.5,
                                      self._height * (1 - base),
                                      self._width * 0.5,
                                      self._height * base,
                                      duration
                                      )
        except Exception as e:
            self.screenshots()
            logger.error('向上滑动失败：{}'.format(e))

    # 从上向下滑动
    def swipe_to_down(self, n=1, base=0.1, duration=1000, text_element=None):
        '''
        从上向下滑动
        :param n: 滑动次数，默认为1
        :param base:辅助参数，忽略
        :param duration:滑动持续时间
        :param text_element:需要滑动的控件
        :return:None
        '''
        try:
            for i in range(n):
                if text_element != None:
                    x_left, x_right, y_top, y_down, x_center, y_center = self._get_element_size(text_element)
                    self.driver.swipe(x_center,
                                      y_down * base,
                                      x_center,
                                      y_down * (1 - base),
                                      duration
                                      )
                else:
                    self.driver.swipe(self._width * 0.5,
                                      self._height * base,
                                      self._width * 0.5,
                                      self._height * (1 - base),
                                      duration
                                      )
        except Exception as e:
            self.screenshots()
            logger.error('向下滑动失败：{}'.format(e))

        # try:
        #     for i in range(n):
        #         self.driver.swipe(self._width * 0.5,
        #                           self._height * base,
        #                           self._width * 0.5,
        #                           self._height * (1 - base),
        #                           duration
        #                           )
        # except Exception as e:
        #     self.screenshots()
        #     logger.error('向下滑动失败：{}'.format(e))

    # 从左向右滑动
    def swipe_to_right(self, n=1, base=0.1, duration=1000, text_element=None):
        '''
        从左向右滑动
        :param n: 滑动次数，默认为1
        :param base:辅助参数，忽略
        :param duration:滑动持续时间
        :param text_element:需要滑动的控件
        :return:None
        '''
        try:
            for i in range(n):
                if text_element != None:
                    x_left, x_right, y_top, y_down, x_center, y_center = self._get_element_size(text_element)
                    self.driver.swipe(x_right * base,
                                      y_center,
                                      x_right * (1 - base),
                                      y_center,
                                      duration
                                      )
                else:
                    self.driver.swipe(self._width * base,
                                      self._height * 0.5,
                                      self._width * (1 - base),
                                      self._height * 0.5,
                                      duration
                                      )
        except Exception as e:
            self.screenshots()
            logger.error('向右滑动失败：{}'.format(e))

        # try:
        #     for i in range(n):
        #         self.driver.swipe(self._width * base,
        #                           self._height * 0.5,
        #                           self._width * (1 - base),
        #                           self._height * 0.5,
        #                           duration
        #                           )
        # except Exception as e:
        #     self.screenshots()
        #     logger.error('向右滑动失败：{}'.format(e))

    # 从右向左滑动
    def swipe_to_left(self, n=1, base=0.1, duration=1000, text_element=None):
        '''
        从右向左滑动
        :param n: 滑动次数，默认为1
        :param base:辅助参数，忽略
        :param duration:滑动持续时间
        :param text_element:需要滑动的控件
        :return:None
        '''
        try:
            for i in range(n):
                if text_element != None:
                    x_left, x_right, y_top, y_down, x_center, y_center = self._get_element_size(text_element)
                    self.driver.swipe(x_right * (1 - base),
                                      y_center,
                                      x_right * base,
                                      y_center,
                                      duration
                                      )
                else:
                    self.driver.swipe(self._width * (1 - base),
                                      self._height * 0.5,
                                      self._width * base,
                                      self._height * 0.5,
                                      duration
                                      )
        except Exception as e:
            self.screenshots()
            logger.error('向左滑动失败：{}'.format(e))

        # try:
        #     for i in range(n):
        #         self.driver.swipe(self._width * (1 - base),
        #                           self._height * 0.5,
        #                           self._width * base,
        #                           self._height * 0.5,
        #                           duration
        #                           )
        # except Exception as e:
        #     self.screenshots()
        #     logger.error('向左滑动失败：{}'.format(e))
