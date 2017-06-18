#! /usr/bin/python
# -*- coding=utf-8 -*-


"""
非阻塞socket的使用(此程序在ubuntu linux和windows xp上测试,Windows可以支持select.select)
监控socket的三个list:in/out/err
程序以5000ms的时间长度为间隔,如果有客户端的请求,接收连接并进行显示;如果没有的话,
每隔5000ms显示一次"no data coming"
"""
import socket,select


class SocketListener:


    """
    构造方法
    """
    def __init__(self,host="",port=50000):
        self.host = host
        self.port = port

    """ 
    无限循环，每5秒监听一次
    """
    def initLsnr01(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        while 1:
            infds, outfds, errfds = select.select([s, ], [], [], 5)
            # 如果infds状态改变,进行处理,否则不予理会
            if len(infds) != 0:
                print 'len(infds): ' + str(len(infds))
                clientsock, clientaddr = s.accept()
                buf = clientsock.recv(8196)
                if len(buf) != 0:
                    print (buf)
                # 不明白在该处关闭clientsock的含义
                # clientsock.close()

            print "no data coming"


    """ 
    循环10次，每次3秒一监控 
    """
    def inistLsnr02(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)

        endFlag = 0
        while endFlag < 10:

            endFlag += 1

            # 通过select 来进行监听:
            infds, outfds, errfds = select.select([s, ], [], [], 3)

            # 如果infds状态改变,进行处理,否则不予理会
            if len(infds) != 0:
                print 'len(infds): ' + str(len(infds))
                clientsock, clientaddr = s.accept()
                buf = clientsock.recv(8196)
                if len(buf) != 0:
                    print (buf)
                # 不明白在该处关闭clientsock的含义
                clientsock.close()

            print "[%s]:%s " %('endFlag', endFlag) + "no data coming"




if __name__ == '__main__':
    thisObj = SocketListener()
    thisObj.inistLsnr02()

