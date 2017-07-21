#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   启动入口

import time

class WechatReply():
    _Tpl ="""
    <xml> 
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>
    """
    _openid=""
    _appid=""

    def __init__(self,openid,appid):
        self._appid=appid
        self._openid=openid

    def reply(self,data):
        CreateTime = int(time.time())
        out =self._Tpl % (self._openid, self._appid, CreateTime, "hello")
        return out

class WechatReplyNews(WechatReply):
    _Tpl ="""
    <xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[news]]></MsgType>
    <ArticleCount>%s</ArticleCount>
    <Articles>
    %s
    </Articles>
    </xml>
    """

    _newsItemTpl="""
    <item>
    <Title><![CDATA[%s]]></Title> 
    <Description><![CDATA[%s]]></Description>
    <PicUrl><![CDATA[%s]]></PicUrl>
    <Url><![CDATA[%s]]></Url>
    </item>
    """
    
    _items=""

    _item_num=0

    def __init__(self,openid,appid):
        self._appid=appid
        self._openid=openid

    def reply(self,data):
        CreateTime = int(time.time())
        out =self._Tpl % (self._openid, self._appid, CreateTime,self._item_num,self._items)
        return out

    def add_newsitem(self,Title, Description, PicUrl, Url):
        """回复文本消息模板"""
        self._item_num+= 1
        out =self._newsItemTpl % (Title, Description, PicUrl, Url)
        self._items=self._items+out