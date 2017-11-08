#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器
from app import *
web_handlers = [
        (r"/api/p/trainSearch/del/(.*)",TrainSearchHandler),
        (r"/api/p/trainSearch/add",TrainSearchHandler),
        (r"/api/p/trainSearch/edit",TrainSearchHandler),
        (r"/api/p/trainSearch/page",TrainSearchHandler),
        (r"/api/p/msg/del/(.*)",WechatMsgHandler),
        (r"/api/p/msg/add",WechatMsgHandler),
        (r"/api/p/msg/edit",WechatMsgHandler),
        (r"/api/p/msg/page",WechatMsgHandler),
        ]