#!/usr/bin/python
# -*- coding: utf-8 -*-
# 函数的目的： 提高程序的重复可用性。


print '-------------函数的定义----------------'
# 定义一个求和函数
def square_sum(a,b):
    c = a**2 + b**2
    # 返回c的值，也就是输出的功能。Python的函数允许不返回值，也就是不用return。
    return c


def square_sum(a,b):
    c = a**2 + b**2
    # return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。
    # 相当于 return (a,b,c)
    return a,b,c


print '-------------函数调用和参数传递----------------'
print square_sum(3,4)
result = square_sum(3,4)
print result, type(result)


print '-------------demo1----------------'
print '-------------值传递----------------'
# 对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。
a = 1

def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
print a

print '-------------demo2----------------'
print '-------------引用/指针传递----------------'
# 对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。
b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print change_list(b)
print b