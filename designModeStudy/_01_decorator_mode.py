#! /usr/bin/python
# -*- coding=utf-8 -*-


import functools



def demo(func):
    print func,type(func)
    print 'zzzz'


"""
1.
无参数函数的装饰器实现：
"""
def deco(func):
    print func, type(func)
    @functools.wraps(func)
    def _deco():
        print("---before myfunc() called.")
        func()
        print("---after myfunc() called.")
        return func
    return  _deco


@deco
def myfunc():
    print "myfunc() called."


"""
2.
带参数的装饰器实现：
"""
def deco2(func):
    print func, type(func)
    def _deco2(c, d):
        print "before myfunc2() called."
        ret = func(c, d)
        print "after myfunc2() called. result: %s" % ret
        return ret
    return _deco2

@deco2
def myfunc2(a ,b):
    print("myfunc(%s,%s) called." % (a, b))
    return a + b


"""
3. 对参数不确定的函数进行装饰
"""
def deco3(func):
    print func, type(func)
    def _deco3(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco3


@deco3
def myfunc3(a ,b):
    print("myfunc(%s,%s) called." % (a, b))
    return a + b

@deco3
def myfunc4(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c







if __name__ == "__main__":

    print myfunc.__name__
    print myfunc.__doc__
    print myfunc.__module__



    pass