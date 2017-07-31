#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from tornado.web import RequestHandler
import tornado.escape
from core.model.core import db
import logging

class BaseHandler(RequestHandler):
    def prepare(self):
        db.connect()
        logging.info(">>>>>>>>>>>>>>>>>>>>>>>> db conn")

    def on_finish(self):
        db.close()
        logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>> db close")
