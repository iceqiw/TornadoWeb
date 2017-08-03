#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器
from app import *
from wechat import WechatEnter

web_handlers = [
        (r"/api/index", IndexHandler),
        (r"/api/user/(\w+)",UserHandler),
        (r"/api",LoginHandler),
        (r"/api/wechat", WechatEnter),
        ]