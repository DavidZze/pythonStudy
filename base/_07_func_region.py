# -*- coding=utf-8 -*-


# python 函数的作用域


def change_param():
    print a
    # 修改a的值
    a = 2

a = 1
change_param()
print a