#! /usr/bin/python
# -*- coding: utf-8 -*-


from base._02_method_demo import MethodDemo
# import __builtin__
from  builtinStudy._01_buitin_module import BuiltinDemo

from _1_no_main_test import  NoMainCls

import sys



if __name__ == '__main__':
    method_obj = MethodDemo()
    method_obj._xxxMethod()

    # # 内建模块中自定义方法的测试
    # BuiltinDemo()
    # # __builtin__.method_a1('aaa', 'bbb')
    # method_a1('aaa', 'bbb') # 合法，但是IDE没有识别
    # # __builtin__.method_c1('aaa3', 'bbb3')
    # method_c1('aaa2', 'bbb2') # 合法，但是IDE没有识别
    #
    # BuiltinDemo.method_c('zzzz', 'zz232')

    no_main_cls = NoMainCls()
    no_main_cls.method_a()

    print sys.path
    sys.path.pop(0)
    print sys.path