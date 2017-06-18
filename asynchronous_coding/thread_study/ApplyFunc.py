#! /usr/bin/python
# -*- coding=utf-8 -*-



# 不带参数的方法
def say():
    print 'say in'



# 函数只带元组的参数
def say(a, b):
    print a, b


# 函数带关键字参数
def say(a=1, b=2):
    print a, b


def haha(**kw):
    print kw
    apply(say, (), kw)




if __name__ == '__main__':
    apply(say)
    apply(say, ('hello', '虫师'))
    haha(a='a', b='b')