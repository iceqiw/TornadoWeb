#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

import logging
import os
import uuid
from core import *
import tornado.escape
from ..service import queryService
_SESSION_COOKIE_KEY = "__SESSION__"


class IndexHandler(BaseHandler):
    def get(self):
        openid = self.get_argument('openid')
        logging.info('{}！'.format(self.request.remote_ip))
        self.set_secure_cookie(_SESSION_COOKIE_KEY, openid)
        self.redirect('http://smartfutuer.xin')

class UserHandler(BaseHandler): 
    def get(self, name):
        logging.info('{}！'.format(self.get_secure_cookie(_SESSION_COOKIE_KEY)))
        respon = {'issuccess': "hello :" + name}
        respon_json = tornado.escape.json_encode(respon)
        queryService.printAll()
        self.write(respon_json)
