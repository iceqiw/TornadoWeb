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


class train_search(BaseModel):
    id = PrimaryKeyField()
    trainNo = CharField(db_column='train_no' )
    date = CharField()
    startStation = CharField(db_column='start_station')
    endStation = CharField(db_column='end_station')

