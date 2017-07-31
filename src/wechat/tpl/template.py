#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   启动入口
'''
a test function module 
'''
import hashlib
import time
from ..core.baseTemplate import WechatReply,WechatReplyNews

m = hashlib.md5()

class WechatReplyRepeat(WechatReply):

    def reply(self,data):
        CreateTime = int(time.time())
        out =self._Tpl % (self._openid, self._appid, CreateTime, data.find("Content").text)
        return out

class WechatReplyNewsA(WechatReplyNews):
    def __init__(self,openid,appid):
        self._appid=appid
        self._openid=openid
        self.add_newsitem("test","teset","https://www.baidu.com/img/bd_logo1.png","https://www.baidu.com/")
        self.add_newsitem("test","teset","","http://smartfutuer.xin/api?openid="+openid)


operator = {"default" : WechatReply, "text_b" : WechatReplyRepeat, "text_g" : WechatReplyNews, "text_o" :WechatReplyNewsA}