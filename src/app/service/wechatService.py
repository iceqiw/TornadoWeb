#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib3
import json
from model.tplModels import *


def save(keyword, content, tplKey):
    Msg.create(keyword=keyword, tplKey=tplKey, content=content)


def update(id, keyword, content, tplKey):
    Msg.update(
        keyword=keyword, tplKey=tplKey,
        content=content).where(Msg.id == id).execute()


def delete(id):
    Msg.delete().where(Msg.id == id).execute()


def findAll():
    return [t for t in Msg.select().dicts()]


def getById(id):
    if id == '0':
        return ''
    return Msg.select().where(Msg.id == id).dicts()[0]