#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib3
import json
from model.appModels import *

def saveTrain(trainNo, date, startStation, endStation):
    train_search.create(
        trainNo=trainNo,
        date=date,
        startStation=startStation,
        endStation=endStation)

def updateTrain(id,trainNo, date, startStation, endStation):
    train_search.update(
        trainNo=trainNo,
        date=date,
        startStation=startStation,
        endStation=endStation).where(train_search.id == id).execute()
        
def deleteTrain(id):
    train_search.delete().where(train_search.id == id).execute()

def searchTrain():
    listTrain=[]
    for t in train_search.select():
        listTrain.append(search(t.id,t.date,t.startStation,t.endStation,t.trainNo))
    return listTrain

def findAllSearchTrain():
    return [t for t in train_search.select().dicts()]

def getByid(id):
    if id=='0' :
        return ''
    return train_search.select().where(train_search.id == id).dicts()[0]