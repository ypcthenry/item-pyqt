#!/usr/bin/env python
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('home/thenry/code/pyqt')
try:
	conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='logindialog',charset='utf8')
	try:
		cur=conn.cursor()
		cur.execute(r'select * from login')
		allperson=cur.fetchall()
	finally:
		cur.close()
		conn.close()
except Exception,e:
	print 'database error:',e
