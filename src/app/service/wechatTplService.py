#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib3
import json
from model.tplModels import *
from config import logger

def save( message, tplKey):
    Tpl.create(tplKey=tplKey, message=message)


def update(id, message, tplKey):
    Tpl.update(
        tplKey=tplKey,
        message=message).where(Tpl.id == id).execute()


def delete(id):
    Tpl.delete().where(Tpl.id == id).execute()


def findAll():
    try:
        return [t for t in Tpl.select().dicts()]
    except Exception as err:
        logger.info(err)
    


def getById(id):
    if id == '0':
        return ''
    return Tpl.select().where(Tpl.id == id).dicts()[0]