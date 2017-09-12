#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from model.userModels import *
from config import logger


def printAll():
    for h in User.select():
        logger.info(h.username)


def isOk(u, p):
    try:
        tmp = User.select().where(User.username==u).get()
        logger.info(tmp)
        if tmp.password == p:
            return True
    except:
        return False
    return False


def saveTpl(key, tpl):
    User.create(owner=uncle_bob, name='Kitty', animal_type='cat')


def search(topic):
    topic = '%' + topic + '%'
    return [k for k in Jx.select().where(Jx.question % topic).dicts()]
