#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com

import hashlib
from tornado.web import RequestHandler
import xml.etree.ElementTree as ET
import time
import logging
from .service import WeChatService

class WechatEnter(RequestHandler):

    def get(self):
        try:
            signature = self.get_argument('signature')
            timestamp = self.get_argument('timestamp')
            nonce = self.get_argument('nonce')
            echostr = self.get_argument('echostr')
            logging.debug('微信sign校验,signature=' + signature + ',&timestamp=' +
                         timestamp + '&nonce=' + nonce + '&echostr=' + echostr)
            result = self.check_signature(signature, timestamp, nonce)
            if result:
                logging.debug('微信sign校验,返回echostr=' + echostr)
                self.write(echostr)
            else:
                logging.error('微信sign校验,---校验失败')
        except Exception as e:
            logging.error('微信sign校验,---Exception' + str(e))

    def check_signature(self, signature, timestamp, nonce):
        """校验token是否正确"""
        token = 'test123465'
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        logging.debug('sha1=' + sha1 + '&signature=' + signature)
        return sha1 == signature

    def post(self):
        body = self.request.body
        logging.debug('微信消息回复中心】收到用户消息' + str(body.decode('utf-8')))
        data = ET.fromstring(body)
        service=WeChatService()
        out=service.process(data)
        self.write(out)
