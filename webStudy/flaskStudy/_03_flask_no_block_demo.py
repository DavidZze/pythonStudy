#! /usr/bin/python
# -*- coding=utf-8 -*-


from flask import Flask
import time
from restfultools import *

from gevent import monkey
from gevent.pywsgi import WSGIServer


"""
测试结论：
flask + gevent 可以做到非阻塞的接收客户端的请求：
"""




# gevent的猴子魔法
monkey.patch_all()

app = Flask(__name__)



@app.route('/api/handler', methods=['GET'])
def asyc_handler():
    """
    阻塞测试：
    :return:
    """
    print get_curr_time()
    long_time_func()
    return fullResponse(R200_OK, "call test_asyc_handler() finished")

def get_curr_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def long_time_func():
    time.sleep(10)


@app.route('/api/author', methods=['GET'])
def get_author():
    return fullResponse(R200_OK, "zhozue--- update")



if __name__ == '__main__':
    # app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()