#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from tornado.web import RequestHandler, Finish
import tornado.escape
from ..model.baseModel import db
from config import logger
import json
from datetime import datetime 

class DateEncoder(json.JSONEncoder ):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj)  
  
class BaseHandler(RequestHandler):
    def prepare(self):
        if db.is_closed():
            db.connect()
            logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> db open')

    def write_success(self, data="success"):
        self.set_header("Content-type", "application/json;charset=utf-8")
        res = {}
        res['data'] = data
        res['code'] = 200
        self.write(tornado.escape.json_encode(res))
        raise Finish  # 确保后面的代码不会执行

    def write_successList(self, data=[]):
        self.set_header("Content-type", "application/json;charset=utf-8")
        try:
            self.write(json.dumps(data, cls=DateEncoder)  )
        except Exception as err:
            logger.info(err)
        
        raise Finish  # 确保后面的代码不会执行

    def on_finish(self):
        if not db.is_closed():
            db.close()
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>> db close")
