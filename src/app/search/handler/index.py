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

class IndexHandler(BaseHandler):
    def get(self):
        self.redirect(page_host)

class UserHandler(BaseHandler): 
    def get(self, name):
        respon = {'issuccess': "hello :" + name}
        respon_json = tornado.escape.json_encode(respon)
        queryService.printAll()
        self.write(respon_json)
