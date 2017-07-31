#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
from ..tpl.template import *

class WechatMsgRouter():
    
    def route(self,openid,appid,handler,data):
        clazz=operator.get(handler)
        try:
            replyOP=clazz(openid,appid)
            return replyOP.reply(data)
        except:
            replyOP=operator.get("default")(openid,appid)
            return replyOP.reply(data)

class WeChatService():

    def __parse(self,data):
        appid = data.find('ToUserName').text
        openid= data.find('FromUserName').text
        msgType = data.find('MsgType').text
        return openid,appid,msgType

    def process(self,data):
        openid,appid,msgType=self.__parse(data)
        if msgType=='event':
            event = data.find('Event').text
            return self._processEvent(openid,appid,event,data)
        else:
            return self._processMsg(openid,appid,msgType,data)

    def _processEvent(self,openid,appid,event,data):
        return self._processMsg(openid,appid,event,data)

    def _processMsg(self,openid,appid,msgType,data):
        router=WechatMsgRouter()
        handler=msgType
        if msgType=='text':
            handler=msgType+'_'+data.find("Content").text
        return router.route(openid,appid,handler,data)
