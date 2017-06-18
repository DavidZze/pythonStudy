#!/usr/bin/python
# -*- coding: utf-8 -*-

laugh = 'zzzzz'


def show_laugh(param):
    laugh = 'llllll'
    print laugh + '1'


class Human1(object):
    print 'object:' , object
    laugh = 'hahaha1'
    def show_laugh(self):
        print laugh
    def laugh_100th(self):
        for i in range(5):
            show_laugh('xxx')

#
class Human2(object):
    print 'object:' , object
    laugh = 'hahaha2'
    def show_laugh(self):
        print laugh
    def laugh_100th(self):
        for i in range(5):
            self.show_laugh()


print '----------Human------------'
zhouze_ze = Human1()
zhouze_ze.laugh_100th()



print '----------Human2------------'
zhouze_ze = Human2()
zhouze_ze.laugh_100th()