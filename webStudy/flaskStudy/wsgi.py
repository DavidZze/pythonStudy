#! /usr/bin/python
# -*- coding: UTF-8 -*-

import _03_flask_block_demo
import eventlet
eventlet.monkey_patch()

def create_app():
  # 这个工厂方法可以从你的原有的 `__init__.py` 或者其它地方引入。
  app = _03_flask_block_demo.app
  return app

application = create_app()



print "__name__::::",__name__
if __name__ == '__main__':
    application.run()



