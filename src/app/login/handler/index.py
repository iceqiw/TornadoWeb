#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器
from tornado.web import RequestHandler
import logging
import os
from core import *

class LoginHandler(RequestHandler):
    _SESSION_COOKIE_KEY = "__SESSION__"

    def get(self):
        try:
            openid = self.get_argument('openid')
            self.set_secure_cookie(self._SESSION_COOKIE_KEY, openid,expires_days=1)
            self.redirect(page_host+'api/index')
        except:
            self.redirect(page_host+'#/allDeposit')


    def post(self):
        openid = self.get_argument('openid')
        logging.info('{}！'.format(self.request.remote_ip))
        self.set_secure_cookie(self._SESSION_COOKIE_KEY, openid,expires_days=1)
        self.redirect(page_host+'api/index')


