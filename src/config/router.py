#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器
from app import *
from wechat.wechatHandler import WechatEnter

web_handlers = [
        (r"/api/user/login",LoginHandler),
        (r"/api/jxSearch/search/(.*)",SearchHandler),
        (r"/api/train/search/(.*)/(.*)/(.*)/(.*)",SearchTrainHandler),
        (r"/api/jxSearch/a/(.*)/(.*)",IndexHandler),
        (r"/wechat/g", WechatEnter),
        ]