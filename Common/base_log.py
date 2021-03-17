#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import os
import time


class Logger:

    def __init__(self):
        self.logger = logging.getLogger()

        # 设置日志可输出的最低级别
        self.logger.setLevel(logging.DEBUG)

        # 输出标准格式设置
        format_ = logging.Formatter(
            '%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s'
        )

        # 日志存储路径设置
        path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../TestLogs'))
        file = time.strftime('%Y-%m-%d %H:%M:%S') + '-' + 'log.txt'
        log_path = os.path.join(path + '/' + file)

        # 创建FileHandler，用于写入日志
        fh = logging.FileHandler(log_path)
        fh.setFormatter(format_)
        fh.setLevel(logging.INFO)

        # 创建StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setFormatter(format_)
        ch.setLevel(logging.INFO)

        # 添加输出文件输出
        self.logger.addHandler(fh)

        # 添加控制台输出
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

    # def debug(self,msg,*args,**kwargs):
    #     self.logger.debug(msg,*args,**kwargs)
    #
    # def info(self, msg, *args, **kwargs):
    #     self.logger.info(msg, *args, **kwargs)
    #
    # def warning(self,msg,*args,**kwargs):
    #     self.logger.warning(msg,*args,**kwargs)
    #
    # def error(self,msg,*args,**kwargs):
    #     self.logger.error(msg,*args,**kwargs)
    #
    # def critical(self,msg,*args,**kwargs):
    #     self.logger.critical(msg,*args,**kwargs)


logger = Logger().get_logger()

'''
import logging

# 第一步，创建日志记录器
# 1，创建一个日志记录器logger
logger = logging.getLogger()
# 2，设置日志记录器的日志级别，这里的日志级别是日志记录器能记录到的最低级别，区别于后面Handler里setLevel的日志级别
logger.setLevel(logging.DEBUG)

# 输出标准格式设置
format_ = logging.Formatter(
    '%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s'
)

# 日志存储路径设置
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../TestLogs'))
file = time.strftime('%Y-%m-%d %H:%M:%S') + '-' + 'log.txt'
log_path = os.path.join(path + '/' + file)

# 第二步，创建日志处理器Handler。这里创建一个Handler，用于将日志写入文件
# 创建FileHandler，用于写入日志文件
fh = logging.FileHandler(log_path)

# 设置保存至文件的日志等级
fh.setLevel(logging.INFO)

# 设置写入日志文件的Handler的日志格式
fh.setFormatter(format_)

# 第三步，将Handler添加至日志记录器logger里
logger.addHandler(fh)

# 同样的，创建一个Handler用于控制台输出日志
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(format_)
logger.addHandler(ch)
'''
