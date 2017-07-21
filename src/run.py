#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   启动入口
import os
import tornado.web
import tornado.httpserver
from tornado.options import define, options
import controller.index as index
import wechat.core.wechatHandler as wx

settings = {'cookie_secret': 'e440769943b4e8442f09de341f3fea28462d2341f483a0ed9a3d5d3859f==78d',
            'session_secret': "3cdcb1f07693b6e75ab50b466a40b9977db123440c28307f428b25e2231f1bcc",
            'session_timeout': 3600,
            'port': 19999,
            }
 
web_handlers = [
        (r"/api/index", index.indexHandler),
        (r"/api/wechat", wx.wechatEnter),
        (r"/api/user/(\w+)",index.userHandler),
        (r"/api", index.LoginHandler),
        ]

define("port", default=settings['port'], help="run on the given port", type=int)

if __name__ == "__main__":

    app = tornado.web.Application(web_handlers, **settings)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
