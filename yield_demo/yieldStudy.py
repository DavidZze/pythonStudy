#! /usr/bin/python
# -*- coding=utf-8 -*-


def g(n):
    """
    yiled 会生成一个Generator对象
    :param n:
    :return:
    """
    for i in range(n):
        yield i **2

for i in g(5):
    print i, ":"

print g(5), type(g(5))




def fab(max):
    """
    Fibonacci
    最大值小于20的斐波拉契数列
    :param max:
    :return:
    """
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a+b


for i in fab(20):
    print i,",",