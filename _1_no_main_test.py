#! /usr/bin/python
# -*- coding: utf-8 -*-


from  builtinStudy._01_buitin_module import BuiltinDemo

"""
模拟非入口模块，
被_0_main_test 所调用
"""
class NoMainCls:

    def __init__(self):
        pass

    def method_a(self):
        # 内建模块中自定义方法的测试
        BuiltinDemo()
        # __builtin__.method_a1('aaa', 'bbb')
        method_a1('aaa', 'bbb')  # 合法，但是IDE没有识别
        # __builtin__.method_c1('aaa3', 'bbb3')
        method_c1('aaa2', 'bbb2')  # 合法，但是IDE没有识别

        BuiltinDemo.method_c('zzzz', 'zz232')