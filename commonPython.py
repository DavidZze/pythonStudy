#! /usr/bin/python
# -*- coding: utf-8 -*-

import time,socket,os,hashlib
import types


class DemoPython:


    task = None


    def __init__(self):
        pass

    """
    1.
    生成md5随机数
    """
    def uniq_flag(self):
        """
        calcute an uniq flag string
        # TODO: can I use uuid here?
        """
        now = int(time.time())
        host = socket.getfqdn()
        pid = os.getpid()
        return self.calc_md5(str(now) + str(host) + str(pid))

    def calc_md5(self, key):
        """Calculate md5
        """
        m = hashlib.md5()
        m.update(key)
        return m.hexdigest()


    """
    2.
    types.ListType
    """
    def listType(self):
        a = [111,222,333,4444]
        a.append(555)
        print a , type(a)
        print type(a) is not types.ListType




    def printTask(self):
        print self.task, type(self.task)


    """
    3.
    初始化值的陷阱：
    python方法的参数是在方法定义的时候即初始化的，
    参考：http://blog.sina.com.cn/s/blog_8a18c33d01019yj2.html
    备注：
    list, dict都是引用类型，这是问题的本质，如果是int就不会出现问题。
    引用类型的值存在另一个内存块。
    """
    def foo(self, numbers=[]):
        numbers.append(9)
        print numbers

    """ 改进后 """
    def foo(numbers=None):
        if numbers is None:
            numbers = []
        numbers.append(9)
        print numbers



if __name__ == '__main__':
    DemoPython.task = '1234'
    thisObj = DemoPython()
    # thisObj.task = 'abcd'
    thisObj.printTask()
    print thisObj.__class__

    #1.
    a = thisObj.uniq_flag()
    print a, type(a)

    #2.
    thisObj.listType()

    #3.
    # thisObj.foo(numbers=[1,2])
    # thisObj.foo([1,2])