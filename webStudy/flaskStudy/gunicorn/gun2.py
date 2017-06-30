# -*- coding=utf-8 -*-


import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing
import os




base_path = os.path.dirname(os.path.abspath(__file__))


bind = '127.0.0.1:5000'
x_forwarded_for_header = 'X-FORWARDED-FOR'
# 超时时间，单位:seconds
# 超时指的是当前worker进程超时，处理超时gunicorn会kill当前进程。
timeout=20


# 日志配置(日志存放的目录必须存在，因为gunicorn不会辅助创建目录（Mac上测试），日志文件则可以交由gunicorn管理)
debug = True
loglevel = 'debug'
pidfile = base_path+ '/log/gunicorn.pid'
accesslog = base_path + '/log/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = base_path + '/log/err.log'
# Redirect stdout/stderr to Error log.
capture_output = True


#启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
# sync, gevent,meinheld gunicorn.workers.ggevent.GeventWorker , gunicorn.workers.base.Worker
worker_class = 'gunicorn.workers.ggevent.GeventWorker'




if __name__ == '__main__':
    print os.path.abspath(__name__)
    dir = os.path.dirname(os.path.abspath(__name__))
    print dir
    print dir.rstrip("/") + "/log/" + "all.out"