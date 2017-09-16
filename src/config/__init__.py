#! /usr/bin/env python
# coding: utf-8
import logging    
import logging.config    
    
logging.config.fileConfig("logger.conf")    # 采用配置文件     
    
# create logger     
logger = logging.getLogger("simpleExample")

from core.model.baseModel import db
from model.appModels import *
from model.tplModels import *
db.create_tables([Msg,TrainSearch], safe=True)