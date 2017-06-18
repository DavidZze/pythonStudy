#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
import sys



class stderrLogging:

    def __init__(self):
        self.adapter = None # 需要init方法进行初始化
        pass

    def initLogging(self):
        # 增加logging 的变量
        prefix_dict = {"prefix": 'stone-runtime'}
        self.adapter = logging.LoggerAdapter(logging.getLogger(), prefix_dict)

        log_fmt = '[-stone-runtime-log] File:\"%(filename)s\" [%(asctime)s] line:%(lineno)s %(levelname)s:%(message)s'
        stderr_log_fmt = "%(prefix)s => " + log_fmt

        # 增加输出到标准错误（stderr）

        logging.basicConfig(level=logging.WARNING,
                            format=stderr_log_fmt,
                            stream=sys.stderr)

    def testLogging(self):
        # 测试
        self.adapter.debug('4-----this is a debug-level msg')
        self.adapter.info('4-----this is a info-level msg')
        self.adapter.warning('4-----this is a warning-level msg')
        self.adapter.error('5-----this is a error-level msg')

        sys.stderr.write('zzzzz-----')



if __name__ == '__main__':
    thisObj = stderrLogging()
    thisObj.initLogging()
    thisObj.testLogging()