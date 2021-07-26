#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import shlex
import signal
import subprocess

import pytest


@pytest.fixture()
def login():
    pass


# 录屏，需要先下载scrcpy插件
# @pytest.fixture(scope="class", autouse=True)  # autouse主动调动的意思，不加这个需要在test_case中写上pytest.fixture
def record():
    cmd = shlex.split("scrcpy --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)


@pytest.fixture(scope='module')  # 在模块运行之前运行
def open():
    print("打开浏览器")
    yield

    print("执行teardown")
    print("关闭浏览器")


def test_search1(open):
    print("test_search1")
    raise NameError
    pass


def test_search2(open):
    print("test_search2")
    pass


def test_search3(open):
    print("test_search3")
    pass


if __name__ == '__main__':
    pytest.main()
