#! /usr/bin/python
# -*- coding=utf-8 -*-

def funcD(a, b, *c):
    print a
    print b
    print "length of c is: %d " % len(c)
    print c


def funcD2(a, b, *c, **d):
    print a
    print b
    print "length of c is: %d " % len(c)
    print c

    for x in d:
        print x + ": " + str(d[x])



if __name__ == "__main__":
    funcD(1,2,3,4,5,6,7,8)

    print "*"*40
    funcD2(1, 2, 3, 4, 5, 6, 7, 8)

    print "*"*40
    funcD2(1, 2, 3, 4, 5, j=6, w=7, u=8)

