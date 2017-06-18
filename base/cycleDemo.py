#!/usr/bin/python
# -*- coding: utf-8 -*-

# 遍历for循环
for a in [3,4.4,'life']:
    print a

print '-----------------------------'
# 建立表
# 这个函数的功能是新建一个表。这个表的元素都是整数，从0开始，下一个元素比前一个大1， 直到函数中所写的上限 （不包括该上限本身）
idx = range(5)
print idx

print '-----------------------------'
print range(10)
for a in range(10):
    print  str(a) + '的3次方是:', a**3


print '-------------while----------------'
i = 2
while i < 10:
    print i
    i = i + 1

print '-------------continue----------------'
# 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作
for i in range(10):
    if i == 2:
        continue
    print i

print '-------------break----------------'
for i in range(10):
    if i == 2:
        break
    print i