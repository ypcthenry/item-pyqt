#!/usr/bin/env python
# coding=utf-8
import sys
import MySQLdb
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import con
class QueryItem(QWidget):
	def __init__(self,parent=None):
		super(QueryItem,self).__init__(parent)
		self.label1=QLabel('要输入的项目编号:'.decode('utf-8'))
		self.lineEdit1=QLineEdit()
		self.label2=QLabel('(小于或等于10)'.decode('utf-8'))
		self.label2.setStyleSheet("QLabel{color:red}")
		self.label1.setBuddy(self.lineEdit1)
		self.button1=QPushButton('查询'.decode('utf-8'))
		self.text1=QTextEdit()
		self.connect(self.button1,SIGNAL("clicked()"),self.query)
		gridlayout=QGridLayout()
		gridlayout.addWidget(self.label1,0,0,1,2)
		gridlayout.addWidget(self.lineEdit1,0,2,1,1)
		gridlayout.addWidget(self.label2,0,3,1,2)
		gridlayout.addWidget(self.button1,1,4)
		gridlayout.addWidget(self.text1,2,0,1,5)
		mainlayout1=QHBoxLayout()
		mainlayout1.addLayout(gridlayout)
		self.setLayout(mainlayout1)
	def query(self):
		try:
			conn3=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
			cur3=conn3.cursor()
			cur3.execute("select id from item")
			result4=cur3.fetchall()
			if (self.lineEdit1.text(),) in result4:
				cur3.execute("select * from item where id = %s",self.lineEdit1.text())
				result1=cur3.fetchall()
				for rec2 in result1:
					self.text1.clear()
					self.text1.insertPlainText('项目编号:'.decode('utf8')+rec2[0]+'\n'+'项目名称:'.decode('utf8')+rec2[1]+\
						'\n'+'负责人:'.decode('utf8')+rec2[2]+'\n'+'所在学院:'.decode('utf8')+rec2[3]+\
						'\n'+'负责人电话:'.decode('utf8')+rec2[4])
			else:
				QMessageBox.warning(self,'NOTICE','此项目不存在'.decode('utf-8'),QMessageBox.Close)
		finally:
			cur3.close()
			conn3.close()
class CreateItem(QWidget):
	def __init__(self,parent=None):
		super(CreateItem,self).__init__(parent)
		self.label1=QLabel('项目编号：'.decode('utf8'))
		self.lineEdit1=QLineEdit()
		self.label2=QLabel('项目名称：'.decode('utf8'))
		self.lineEdit2=QLineEdit()
		self.label3=QLabel('负责人：'.decode('utf8'))
		self.lineEdit3=QLineEdit()
		self.label4=QLabel('所在学院：'.decode('utf8'))
		self.lineEdit4=QLineEdit()
		self.label5=QLabel('负责人电话：'.decode('utf8'))
		self.lineEdit5=QLineEdit()
		self.okbutton=QPushButton('确认添加'.decode('utf8'))
		mainlayout=QGridLayout()
		mainlayout.addWidget(self.label1,0,0,)
		mainlayout.addWidget(self.lineEdit1,0,1,1,2)
		mainlayout.addWidget(self.label2,1,0,)
		mainlayout.addWidget(self.lineEdit2,1,1,1,2)
		mainlayout.addWidget(self.label3,2,0,)
		mainlayout.addWidget(self.lineEdit3,2,1,1,2)
		mainlayout.addWidget(self.label4,3,0,)
		mainlayout.addWidget(self.lineEdit4,3,1,1,2)
		mainlayout.addWidget(self.label5,4,0,)
		mainlayout.addWidget(self.lineEdit5,4,1,1,2)
		mainlayout.addWidget(self.okbutton,5,1)
		self.setLayout(mainlayout)
		self.connect(self.okbutton,SIGNAL("clicked()"),self.update)
	def update(self):
		try:
			conn1=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
			cur1=conn1.cursor()
			cur1.execute("insert into item value(%s,%s,%s,%s,%s)",(self.lineEdit1.text().toUtf8(),self.lineEdit2.text().toUtf8(),self.lineEdit3.text().toUtf8(),self.lineEdit4.text().toUtf8(),self.lineEdit5.text().toUtf8()))
			conn1.commit()
			QMessageBox.warning(self,'NOTICE','添加成功'.decode('utf-8'),QMessageBox.Close)
		finally:
			cur1.close()
			conn1.close()
class ShowItem1(QWidget):
	i=0
	def __init__(self,parent=None):
		super(ShowItem1,self).__init__(parent)
		self.table=QTableWidget(7,5)
		self.table.setHorizontalHeaderLabels(['项目编号'.decode('utf-8'),'项目名称'.decode('utf-8'),'项目负责人'.decode('utf-8'),'所在学院'.decode('utf-8'),'负责人电话'.decode('utf-8')])
		self.button=QPushButton('刷新'.decode('utf8'))
	#	try:
	#		conn2=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
	#		cur2=conn2.cursor()
	#		cur2.execute("select * from item")
	#		result=cur2.fetchall()
	#		for rec1 in result:
	#			self.table.setItem(self.i,0,QTableWidgetItem(rec1[0]))	
	#			self.table.setItem(self.i,1,QTableWidgetItem(rec1[1]))	
	#			self.table.setItem(self.i,2,QTableWidgetItem(rec1[2]))	
	#			self.table.setItem(self.i,3,QTableWidgetItem(rec1[3]))	
	#			self.table.setItem(self.i,4,QTableWidgetItem(rec1[4]))
	#			self.i=self.i+1
	#	finally:
	#		cur2.close()
	#		conn2.close()
		self.connect(self.button,SIGNAL("clicked()"),self.refresh)
		mainlayout=QHBoxLayout()
		mainlayout.addWidget(self.table)
		mainlayout.addWidget(self.button)
		self.setLayout(mainlayout)
	def refresh(self):
		try:
			conn5=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
			cur5=conn5.cursor()
			cur5.execute("select * from item")
			result=cur5.fetchall()
			self.table.clear()
			for rec1 in result:
				self.table.setItem(self.i,0,QTableWidgetItem(rec1[0]))	
				self.table.setItem(self.i,1,QTableWidgetItem(rec1[1]))	
				self.table.setItem(self.i,2,QTableWidgetItem(rec1[2]))	
				self.table.setItem(self.i,3,QTableWidgetItem(rec1[3]))	
				self.table.setItem(self.i,4,QTableWidgetItem(rec1[4]))
				self.i=self.i+1
			self.i=0
		finally:
			cur5.close()
			conn5.close()
class DeleteItem(QWidget):
	def __init__(self,parent=None):
		super(DeleteItem,self).__init__(parent)
		self.label1=QLabel('要删除的项目编号：'.decode('utf8'))
		self.lineEdit1=QLineEdit()
		self.okbutton=QPushButton('确认删除'.decode('utf8'))
		self.connect(self.okbutton,SIGNAL("clicked()"),self.reward)
		mainlayout=QGridLayout()
		mainlayout.addWidget(self.label1,0,0)
		mainlayout.addWidget(self.lineEdit1,0,1,1,2)
		mainlayout.addWidget(self.okbutton,1,2)
		self.setLayout(mainlayout)
	def reward(self):
		try:
			conn4=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
			cur4=conn4.cursor()
			cur4.execute("select id from item")
			result2=cur4.fetchall()
			if (self.lineEdit1.text(),) in result2:
				cur4.execute("delete from item where id = %s",self.lineEdit1.text())
				conn4.commit()
				QMessageBox.warning(self,'NOTICE','删除成功'.decode('utf-8'),QMessageBox.Close)
			else:
				QMessageBox.warning(self,'NOTICE','不存在此项目'.decode('utf-8'),QMessageBox.Close)
		finally:
			cur4.close()
			conn4.close()
class MainWindow(QWidget):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.tab=QTabWidget()
		self.setWindowTitle('项目管理界面'.decode('utf8'))
		self.create=CreateItem()
		self.show1=ShowItem1()
		self.query=QueryItem()
		self.delete1=DeleteItem()
		self.tab.addTab(self.create,'创建'.decode('utf8'))
		self.tab.addTab(self.show1,"显示".decode('utf-8'))
		self.tab.addTab(self.query,"查询".decode('utf-8'))
		self.tab.addTab(self.delete1,"删除".decode('utf-8'))
		mainlayout=QHBoxLayout()
		mainlayout.addWidget(self.tab)
		self.setLayout(mainlayout)
