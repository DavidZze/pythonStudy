#! /usr/bin/python
# -*- coding=utf-8 -*-


import argparse



class MultiCmdArgs:

    def __init__(self):
        pass

    # 位置参数 + 可选参数
    def multiArgsParse01(self):
        parse = argparse.ArgumentParser()
        parse.add_argument("square" ,type = int, help="display a square of a given number")
        parse.add_argument("-v", "--verbose", action = "store_true", help="increase output verbosity")
        args = parse.parse_args()
        answer = args.square ** 2
        if args.verbose:
            print "the square of {} equals {}".format(args.square, answer)
        else:
            print answer


    # 位置参数 + 可选参数
    def multiArgsParse02(self):
        parse = argparse.ArgumentParser()
        parse.add_argument("a", type=int, help="number a")
        parse.add_argument("b", type=int, help="number b")
        parse.add_argument("c", type=int, help="number c")
        parse.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
        args = parse.parse_args()
        a = args.a
        b = args.b
        c = args.c
        answer = a + b + c
        if args.verbose:
            print "the count of a= {} , b= {} , c= {} equals {}".format(args.a, args.b , args.c,  answer)
        else:
            print answer


if 'aaaaaa' :
    print '.....'


if __name__ == '__main__':
    thisObj = MultiCmdArgs()
    # thisObj.multiArgsParse01()
    thisObj.multiArgsParse02()




