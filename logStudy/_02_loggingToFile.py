#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging


# python logging 是系统的模块，

# 1
# 默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# 级别：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# logging.debug('this is a debug-level msg')
# logging.info('this is a info-level msg')
# logging.warning('this is a warning-level msg')

class LoggingToFile:

    def __init__(self):
        pass

    def initLogging(self):
        # 2
        # 通过logging.basicConfig函数对日志的输出格式及方式做相关配置
        logging.basicConfig(level=logging.DEBUG,
                            format='[stone-runtime-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s',
                            filename='/Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/logStudy/myapp.log',
                            filemode='w')

    def testLogging(self):
        logging.debug('2-----this is a debug-level msg')
        logging.info('2-----this is a info-level msg')
        logging.warning('2-----this is a warning-level msg')
        logging.error('3-----this is a error-level msg')


if __name__ == '__main__':
    thisObj = LoggingToFile()
    thisObj.initLogging()
    thisObj.testLogging()