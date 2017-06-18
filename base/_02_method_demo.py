#! /usr/bin/python
# -*- coding=utf-8 -*-

class MethodDemo:


    """
    构造方法/初始化方法：
    实例创建时执行的方法
    """
    def __init__(self):
        print "do __init__()"
        pass

    """
    专有方法：
    表示该方法是专有的
    """
    def __func__(self):
        print 'do __func__(self) '

    """
    私有方法：
    通过实例无法访问到的方法
    """

    def __privateMethod(self):
        print '__privateMethod(self)'

    """
    受保护的方法：
    在子类和本类实例中可以访问的方法
    """
    def _xxxMethod(self):
        print '_xxxMethod(self)'


    """
    类的实例方法：
    类的实例访问的方法
    """
    def instance_method(self):
        print 'I am class instance method'

    """
    析构函数。
    即对象销毁的时候执行的函数
    """
    def __del__(self):
        print "do __del__()"

if __name__ == "__main__":
    thisObj = MethodDemo()

    thisObj._xxxMethod()
    thisObj.instance_method()