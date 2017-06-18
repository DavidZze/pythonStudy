#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import sys




class LoggingMultiOutput2:


    def __init__(self):
        pass

    def initLogging(self):

        # 这一步很关键，loggingHandler的日志级别如果低于该级别则失效。
        logging.getLogger().setLevel(logging.DEBUG)

        # 输出到mylog2.log  INFO以上
        Rthandler = RotatingFileHandler('myapp2.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        Rthandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '[-stone-runtime-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s')
        Rthandler.setFormatter(formatter)

        # 输出到mylog3.log ERROR以上
        Rthandler2 = RotatingFileHandler('myapp3.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        Rthandler2.setLevel(logging.ERROR)
        formatter2 = logging.Formatter(
            '[-stone-runtime-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s')
        Rthandler2.setFormatter(formatter2)

        # 输出到屏幕控制台（stdout）
        StreamingHandler = logging.StreamHandler()
        StreamingHandler.setLevel(logging.WARNING)
        formatter3 = logging.Formatter(
            '[-stone-runtime-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s')
        StreamingHandler.setFormatter(formatter3)

        # 指定日志处理器（每个处理器都有一个输出目的地）
        logging.getLogger().addHandler(Rthandler)
        logging.getLogger().addHandler(Rthandler2)
        logging.getLogger().addHandler(StreamingHandler)

        # 增加输出到标准错误（stderr）
        logging.basicConfig(level=logging.DEBUG,
                            format=formatter3,
                            stream=sys.stderr)


    def testLogging(self):
        # 测试
        logging.debug('4-----this is a debug-level msg')
        logging.info('4-----this is a info-level msg')
        logging.warning('4-----this is a warning-level msg')
        logging.error('5-----this is a error-level msg')


if __name__ == '__main__':
    thisObj = LoggingMultiOutput2()
    thisObj.initLogging()
    thisObj.testLogging()





