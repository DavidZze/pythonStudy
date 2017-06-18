#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging



class LoggingMultiPutput:

    def __init__(self):
        pass

    def initLogging(self):
        # 1
        # 通过logging.basicConfig函数对日志的输出格式及方式做相关配置
        logging.basicConfig(level=logging.DEBUG,
                            format='[stone-runtime-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s',
                            filename='./myapp.log',
                            filemode='w')

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

    def testLogging(self):
        logging.debug('4-----this is a debug-level msg')
        logging.info('4-----this is a info-level msg')
        logging.warning('4-----this is a warning-level msg')
        logging.error('5-----this is a error-level msg')


if __name__ == '__main__':
    thisObj = LoggingMultiPutput()
    thisObj.initLogging()
    thisObj.testLogging()


