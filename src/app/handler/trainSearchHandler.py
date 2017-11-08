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

class TrainSearchHandler(BaseHandler):
    def get(self):
        params = trainService.findAllSearchTrain()
        self.write_successList(params)

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        trainService.saveTrain(**data)
        self.write_success()

    def put(self):
        data = tornado.escape.json_decode(self.request.body)
        trainService.updateTrain(**data)
        self.write_success()

    def delete(self,id):
        trainService.deleteTrain(id)
        self.write_success()