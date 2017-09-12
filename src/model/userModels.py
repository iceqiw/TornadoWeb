#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   qiwei
#   E-mail  :   qqwei1123@163.com
#   Date    :   17/7/15 下午3:54
#   Desc    :   首页控制器

from core import BaseModel
from peewee import *
import datetime


class User(BaseModel):
    id = BigIntegerField(unique=True)
    username = CharField(unique=True)
    password = CharField(unique=True)
    status = BooleanField(unique=True)
    name = CharField(unique=True)


class Jx(BaseModel):
    id = CharField(unique=True)
    itemtype = CharField(unique=True)
    itemno = CharField(unique=True)
    imglink = CharField(unique=True)
    answer = CharField(unique=True)
    question = CharField(unique=True)
    optiona = CharField(unique=True)
    optionb = CharField(unique=True)
    optionc = CharField(unique=True)
    optiond = CharField(unique=True)
