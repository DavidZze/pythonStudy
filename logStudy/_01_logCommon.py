#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging


# python logging 是系统的模块，

# 1
# 默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# 级别：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET


class LogCommon:

    def __init__(self):
        pass

    def testLogging(self):
        logging.getLogger().setLevel(logging.DEBUG)
        print logging.getLogger().getEffectiveLevel()
        logging.debug('this is a debug-level msg')
        logging.info('this is a info-level msg')
        logging.warning('this is a warning-level msg')


if __name__ == '__main__':
    thisObj = LogCommon()
