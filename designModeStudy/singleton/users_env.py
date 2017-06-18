#! /usr/bin/python
# -*- coding=utf-8 -*-

"""
2.
用户环境类 extends BasicEnv
并设计为单例模式。
"""

from basic_env import BasicEnv

"""
装饰器方法：
没有实例则调用UsersEnv 创建构造实例
如果dict中有这个实例则直接返回。
"""
def _singleton(cls, *args, **kwargs):
    instance = {}
    def _singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton

@_singleton
class UsersEnv(BasicEnv):

    def __init__(self):
        print "this is UserEnv Object."
        #1. 需要显示的调用父类的__init__来构造子类
        BasicEnv.__init__(self)
        print "_basic_name=" + self._basic_name




if __name__ == "__main__":
    # thisObj = UsersEnv()
    ins_a = UsersEnv()
    ins_b = UsersEnv()
    print (ins_a == ins_b)

    test_dict = {}
    test_dict[ins_b.__class__] = ins_a
    print test_dict, type(test_dict)
    print test_dict[ins_b.__class__], type(test_dict[ins_b.__class__])