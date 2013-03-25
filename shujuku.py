#!/usr/bin/env python
# coding=utf-8
from PyQt4 import QtSql,QtGui
import sys
db=QSql.QSqlDatabase.addDatabase('QMYSQL')
db.setHostName('losthost')
db.setDatabaseName('logindialog')
db.setUserName('root')
db.setPassword('123456')
dbopen=db.open()

