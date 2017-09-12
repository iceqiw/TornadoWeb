#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from tornado.web import RequestHandler
import tornado.escape
from ..model.baseModel import db
from config import logger

class BaseHandler(RequestHandler):
    _SESSION_COOKIE_KEY = "__SESSION__"
    def prepare(self):
        openid=self.get_secure_cookie(self._SESSION_COOKIE_KEY)
        logger.info('{}！'.format(openid))
        if openid is None:
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>> mo login")
            self.redirect(page_host)
        db.connect()
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>> db conn")

    def on_finish(self):
        logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>> finish")
        if not db.is_closed():
            db.close()
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>> db close")
