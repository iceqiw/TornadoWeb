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
        res = queryService.isOk(username, pwd)
        if res:
            self.session = {
                'name': username,
                'ok': True,
            }
        self.write_success(res)


class IndexHandler(UserHandler):
    def get(self, topic, name):
        logger.info(topic)
        logger.info(name)

class SearchTrainHandler(BaseHandler):
    def get(self,date,start,end,tf):
        lista=[]
        lista.append(trainService.search(date,start,end,tf))
        lista.append(trainService.search(date,'FZS','XAY','T306'))
        lista.append(trainService.search('2017-10-06','BJY','FZS','T308'))
        self.write_success(lista)

class SearchHandler(UserHandler):
    def get(self, topic):
        logger.info(topic)
        alist = queryService.search(topic)
        self.write_success(alist)