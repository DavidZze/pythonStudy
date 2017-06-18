#! /usr/bin/python
# -*- coding=utf-8 -*-

"""
http Server：
模拟服务端接收http请求，处理http请求，并生成http响应报文。
"""
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):


    def _writeheaders(self):
        print self.path
        print self.headers
        self.send_response(200);
        self.send_header('Content-type','text/html');
        self.end_headers()


    def do_Head(self):
        self._writeheaders()


    def do_GET(self):
        self._writeheaders()
        # self.wfile.write("""<!DOCTYPE HTML>
        #                     <html lang="en-US">
        #                     <head>
        #                     <meta charset="UTF-8">
        #                     <title></title>
        #                     </head>
        #                     <body>
        #                         <p>this is get!</p>
        #                     </body>
        #                     </html>"""
        #                  + str(self.headers))
        self.wfile.write('{"code":"1", "msg":"success", "data":"this is get!"}')

    def do_POST(self):
        self._writeheaders()
        length = self.headers.getheader('content-length');
        nbytes = int(length)
        data = self.rfile.read(nbytes)
        # self.wfile.write("""<!DOCTYPE HTML>
        #                     <html lang="en-US">
        #                     <head>
        #                         <meta charset="UTF-8">
        #                         <title></title>
        #                     </head>
        #                     <body>
        #                     <p>this is POST!</p>
        #                     </body>
        #                     </html>""" + str(self.headers)+str(self.command)+str(self.headers.dict)+data)
        self.wfile.write('{"code":"1", "msg":"success", "data":"this is POST!"}')




# 关闭使用的端口的命令： lsof -i:8765 | awk '{print $2}' | grep -v "PID" |  xargs kill -9
# basehttpserver官方文档：https://docs.python.org/2/library/basehttpserver.html
if __name__ == '__main__':
    addr = ('', 8765)
    server = HTTPServer(addr, RequestHandler)
    server.serve_forever()

