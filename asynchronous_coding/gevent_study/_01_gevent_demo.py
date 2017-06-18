#! /usr/bin/python
# -*- coding=utf-8 -*-



from gevent import monkey; monkey.patch_socket()
import gevent



def f(n, a , b ,c ,d):
    print a, b , c , d
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

g1 = gevent.spawn(f, 5 ,4 ,'ss', 2,1)
g2 = gevent.spawn(f, 5 ,4 ,'zz', 2,1)
g3 = gevent.spawn(f,5 ,4 ,'dd', 2,1)
g1.join()
g2.join()
g3.join()






