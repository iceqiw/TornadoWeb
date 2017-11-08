#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器
from tornado.web import RequestHandler
import tornado.escape
from config import logger
from core import *
from ..service import *

class WechatMsgHandler(BaseHandler):
    def get(self):
        params = wechatService.findAll()
        self.write_successList(params)

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        wechatService.save(**data)
        self.write_success()

    def put(self):
        data = tornado.escape.json_decode(self.request.body)
        wechatService.update(**data)
        self.write_success()

    def delete(self,id):
        wechatService.delete(id)
        self.write_success()