#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler




class LoggingRoating:

    def __init__(self, author):
        self.author = author
        pass


    def initLogging(self):

        print 'author: ' + self.author

        # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
        Rthandler = RotatingFileHandler('myapp2.log', maxBytes=10 * 1024 * 1024, backupCount=5)
        Rthandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        Rthandler.setFormatter(formatter)
        logging.getLogger('').addHandler(Rthandler)

    def testLogging(self):
        logging.debug('4-----this is a debug-level msg')
        logging.info('4-----this is a info-level msg')
        logging.warning('4-----this is a warning-level msg')
        logging.error('5-----this is a error-level msg')


if __name__ == '__main__':
    thisObj = LoggingRoating('zhouze')
    thisObj.initLogging()
    thisObj.testLogging()







