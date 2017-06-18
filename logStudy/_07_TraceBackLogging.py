#! /usr/bin/python
# -*- coding: utf-8 -*-


import traceback
import logging



# traceback 模块是python自带的模块，用于当python出现异常时生成
# 异常堆栈信息

class excep_class:

    def __init__ (self):
        pass

    def initLogging(self):
        logging.basicConfig(filename='/Users/zhouze/Documents/AppWorkspace/PycharmProjects/pythonStudy/logStudy/myapp.log')

    def except_fun (self):
        a=12
        b=0
        print(a/b)


if __name__=="__main__":

    thisObj = excep_class()
    thisObj.initLogging()

    try:
        thisObj.except_fun()
    except:
        # traceback.format_exc() 用于格式化异常堆栈，可以自定义格式
        s = traceback.format_exc()
        # 将异常信息（str）输出到logging模块
        logging.error(s)


