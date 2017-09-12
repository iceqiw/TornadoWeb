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


class LoginHandler(BaseHandler):
    def post(self):
        logger.info(">>>>>>>>>>>>>>>>>>>>>>login")
        data = tornado.escape.json_decode(self.request.body)
        pwd = data['password']
        username = data['username']
        res = {}
        res['res'] = queryService.isOk(username, pwd)
        respon_json = tornado.escape.json_encode(res)
        self.write(respon_json)


class IndexHandler(BaseHandler):
    def get(self, topic, name):
        logger.info(topic)
        logger.info(name)


class SearchHandler(BaseHandler):
    def get(self, topic):
        logger.info(topic)
        alist = queryService.search(topic)
        respon_json = tornado.escape.json_encode(alist)
        self.write(respon_json)