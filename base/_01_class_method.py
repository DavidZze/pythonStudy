#! /usr/bin/python
# -*- coding=utf-8 -*-

class ClassMethod(object):

    METHOD = 'method hoho'

    def __init__(self):
        self.name = 'leon'

    """
    类的实例方法
    """
    def test1(self):
        print 'test1'
        print self
        print '----------------'

    """
    类方法
    """
    @classmethod
    def test2(cls):
        print cls
        print 'test2'
        print ClassMethod.METHOD
        print '----------------'

    """
    类的静态方法
    """
    @staticmethod
    def test3():
        print ClassMethod.METHOD
        print 'test3'




if __name__ == '__main__':
    a = ClassMethod()
    b = a
    print id(a) , id(b)


    a.test1()
    a.test2()
    a.test3()
    ClassMethod.test3()