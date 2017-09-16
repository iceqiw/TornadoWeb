#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from tornado.web import RequestHandler,Finish
import tornado.escape
from ..model.baseModel import db
from config import logger
import json


class BaseHandler(RequestHandler):
    """
    基类
    (暂时主要功能是id加盐和用户状态的管理)
    """

    _SESSION_COOKIE_KEY = "__SESSION__"

    def prepare(self):
        if db.is_closed():
            db.connect()
            logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> db open')
        if self.session:
            self.current_user = self.get_user

    @property
    def get_user(self):
        if self.session:
            return json.loads(self.session)
        else:
            return {}

    @property
    def session(self):
        return self.get_secure_cookie(self._SESSION_COOKIE_KEY)

    @session.setter
    def session(self, value):
        if isinstance(value, dict):
            value = json.dumps(value)
        self.set_secure_cookie(self._SESSION_COOKIE_KEY, value, expires_days=1)

    @session.deleter
    def session(self):
        self.clear_cookie(self._SESSION_COOKIE_KEY)

    def write_success(self, data="success"):
        self.set_header("Content-type","application/json;charset=utf-8")
        res={}
        res['data']=data
        res['code']=200
        self.write(tornado.escape.json_encode(res))
        raise Finish  # 确保后面的代码不会执行

    def on_finish(self):
        if not db.is_closed():
            db.close()
            logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>> db close")

class UserHandler(BaseHandler):
    """
    登陆
    """
    def prepare(self):
        # 如果未登陆则跳到首页
        if db.is_closed():
            db.connect()
            logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> db open')
        if self.get_user:
            self.current_user = self.get_user
        else:
            self.send_error(400)
            raise Finish
