#! /usr/bin/python
# -*- coding=utf-8 -*-



class LambdaDemo:

    def __init__(self):
        pass


    """
    1.
    Map_lambda:
    值一一转换的过程。
    """
    def _map_lambda(self):
        # li = {1:11, 2:22, 3:33}
        # li = (11,22,33)
        li = [11,22,33]
        new_list = map(lambda a:a+100, li)
        print new_list

        s1 = [1,2,3]
        new_list = map(lambda a,b:a*2+b, li, s1)
        print new_list



    """
    2.
    filter_lambda:
    以前是什么类型，现在依旧是什么类型，哪怕没有符合条件的。
    """
    def _filter_lambda(self):
        li = [11,22,33]
        new_list = filter(lambda arg:arg>22, li)
        print new_list, type(new_list)

        new_list = filter(lambda  arg:arg>33, li)
        print new_list, type(new_list)


    """
    3.
    reduce_lambda:
    汇总。
    """
    def _reduce_lambda(self):
        li = [11,22,33]
        result = reduce(lambda arg1,arg2:arg1+arg2, li)
        print result, type(result)

        li2 = [11]
        # li2 = []  # exception
        result = reduce(lambda arg1,arg2:arg1+arg2, li2)
        print result, type(result)



if __name__ == "__main__":
    thisObj = LambdaDemo()
    thisObj._map_lambda()

    print "*"*40
    thisObj._filter_lambda()

    print "*"*40
    thisObj._reduce_lambda()