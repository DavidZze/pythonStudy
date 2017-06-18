#! /usr/bin/python
# -*- coding=utf-8 -*-

import __builtin__

class BuiltinDemo:

    def __init__(self):
        __builtin__.method_a1 = self.method_a
        __builtin__.method_b1 = self.method_b
        __builtin__.method_c1 = BuiltinDemo.method_c


    def method_a(self, name, age):
        print 'name1: ' + name, 'age1: ' + age

    def method_b(self, name, age):
        print 'name2: ' + name, 'age2: ' + age

    @staticmethod
    def method_c(name, age):
        print 'name3: ' + name, 'age3: ' + age
