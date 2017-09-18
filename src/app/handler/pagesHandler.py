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
        pwd = self.get_argument('password')
        username = self.get_argument('username')
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
    def get(self):
        trains = trainService.searchTrain()
        self.write_success(trains)


class TrainHandler(BaseHandler):
    def get(self):
        id = self.get_argument('id')
        if id:
            params = trainService.getByid(id)
        else :
            params = trainService.findAllSearchTrain()
        self.write_success(params)

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        trainService.saveTrain(**data)
        self.write_success()

    def put(self):
        data = tornado.escape.json_decode(self.request.body)
        trainService.updateTrain(**data)
        self.write_success()

    def delete(self):
        id = self.get_argument('id')
        trainService.deleteTrain(id)
        self.write_success()


class SearchHandler(UserHandler):
    def get(self, topic):
        logger.info(topic)
        answerList = queryService.search(topic)
        self.write_success(answerList)