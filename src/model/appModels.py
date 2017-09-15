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
    id = PrimaryKeyField()
    username = CharField(unique=True)
    password = CharField()
    status = BooleanField()
    name = CharField()


class Jx(BaseModel):
    id = BigIntegerField()
    itemtype = CharField()
    itemno = CharField()
    imglink = CharField()
    answer = CharField()
    question = CharField()
    optiona = CharField()
    optionb = CharField()
    optionc = CharField()
    optiond = CharField()

class Train(BaseModel):
    id = PrimaryKeyField()
    yz = CharField()
    yw = CharField()
    rw = CharField()
    trainNo = CharField()
    date = CharField()
    startStation = CharField()
    endStation = CharField()

class TrainSearch(BaseModel):
    id = PrimaryKeyField()
    trainNo = CharField()
    date = CharField()
    startStation = CharField()
    endStation = CharField()

class Msg(BaseModel):
    key = CharField(unique=True)
    content = CharField()