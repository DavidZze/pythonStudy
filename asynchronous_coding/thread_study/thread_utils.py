#! /usr/bin/python
# -*- coding=utf-8 -*-



import threading
from time import ctime,sleep




class MyThread(threading.Thread):
    """

    """

    def __init__(self, func, args, kwards, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.kwards = kwards

    def run(self):
        # print self.args,self.kwards
        if self.args != None and self.kwards == None:
            apply(self.func, self.args)
        elif self.args ==None and self.kwards != None:
            apply(self.func, (), self.kwards)
        elif self.args != None and self.kwards != None:
            apply(self.func, self.args, self.kwards)



def tuple_func(file,time):
    """
    type: 元组参数函数：
    测试需将在多个线程中运行的函数
    :param file:
    :param time:
    :return:
    """
    for i in range(2):
        print 'Start playing： %s! %s' % (file, ctime())
        sleep(time)


def kwards_func(a=1, b=2):
    """
    type: 关键字函数：
    测试用户通过参数名的调用方式
    :param a:
    :param b:
    :return:
    """
    print 'kwards_func: ' + a , b



def complex_func(a=1, b=2, c = 3 , d =4):
    """
    type: 位置（元组）+ 关键字
    测试用户通过参数名的调用方式
    :param a:
    :param b:
    :return:
    """
    print 'kwards_func: ' + a , b, c, d



if __name__ == '__main__':
    dict = {'爱情买卖.mp3': 3, '阿凡达.mp4': 3}
    list_files = range(len(dict))
    print list_files

    # 创建线程
    threads = []
    for k, v in dict.items():
        t = MyThread(tuple_func, (k, v), None ,tuple_func.__name__)
        threads.append(t)

    # 启动线程
    for i in list_files:
        threads[i].start()
    # 将子线程加入到主线程中：
    for i in list_files:
        threads[i].join()

    # 主线程执行打印
    print 'end:%s' %ctime()

    print t
    t = MyThread(kwards_func, None, {'a':'aaaa','b':'bbbb'})
    t.start()

    t2 = MyThread(complex_func,('111','222'), {'c':'333', 'd':'444'})
    t3 = MyThread(complex_func, ('111', '222', '333', '4444'), None)
    t4 = MyThread(complex_func, None, {'a':'111', 'b':'222', 'c':'333', 'd':'444'})

    t2.start()
    t3.start()
    t4.start()

