#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : helloworld.py

# 导入系统模块
import sys

print sys.path
print dir(sys)
print 'Hello World'

print([i for i in 'HELLO'])

v = 'a:b:c'
print v[0],v[1],v[2]

v2 = '123456'
print v2[0],v2[-1]