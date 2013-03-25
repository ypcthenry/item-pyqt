#!/usr/bin/env python
# coding=utf-8
import sys
import MySQLdb
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import con
class ShowItem(QWidget):
	def __init__(self,parent=None):
		super(ShowItem,self).__init__(parent)
		self.table=QTableWidget(5,5)
		self.table.setHorizontalHeaderLabels(['项目编号'.decode('utf-8'),'项目名称'.decode('utf-8'),'项目负责人'.decode('utf-8'),'所在学院'.decode('utf-8'),'负责人电话'.decode('utf-8')])
		self.table.setItem(0,0,QTableWidgetItem('01'))
		self.table.setItem(0,1,QTableWidgetItem('01'))
		self.table.setItem(0,2,QTableWidgetItem('01'))
		self.table.setItem(0,3,QTableWidgetItem('01'))
		self.table.setItem(0,4,QTableWidgetItem('01'))
		self.table.setItem(1,0,QTableWidgetItem('01'))
		self.table.setItem(1,1,QTableWidgetItem('01'))
		self.table.setItem(1,2,QTableWidgetItem('01'))
		self.table.setItem(1,3,QTableWidgetItem('01'))
		self.table.setItem(1,4,QTableWidgetItem('01'))
		self.table.setItem(2,0,QTableWidgetItem('01'))
		self.table.setItem(2,1,QTableWidgetItem('01'))
		self.table.setItem(2,2,QTableWidgetItem('01'))
		self.table.setItem(2,3,QTableWidgetItem('01'))
		self.table.setItem(2,4,QTableWidgetItem('01'))
		self.table.setItem(3,0,QTableWidgetItem('01'))
		self.table.setItem(3,1,QTableWidgetItem('01'))
		self.table.setItem(3,2,QTableWidgetItem('01'))
		self.table.setItem(3,3,QTableWidgetItem('01'))
		self.table.setItem(3,4,QTableWidgetItem('01'))
		self.table.setItem(4,0,QTableWidgetItem('01'))
		self.table.setItem(4,1,QTableWidgetItem('01'))
		self.table.setItem(4,2,QTableWidgetItem('01'))
		self.table.setItem(4,3,QTableWidgetItem('01'))
		self.table.setItem(4,4,QTableWidgetItem('01'))
		self.button=QPushButton('刷新'.decode('utf8'))
		self.record=[]
		for i in range(self.table.rowCount()):
			for j in range(self.table.columnCount()):
				if self.table.item(i,j)!=None:
					self.record.append(self.table.item(i,j).text())
		self.connect(self.button,SIGNAL("clicked()"),self.update)
		def update(self):
			for i in range(self.table.rowCount()):
				for j in range(self.table.columnCount()):
					if self.table.item(i,j)!=None:
						self.record[i*5+j]=(sekf.table.item(i,j).text())
		try:
			conn1=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
			cur1=conn1.cursor()
			for j in range(self.table.columnCount()):
				cur1.execute("insert into item value(%s,%s,%s,%s,%s)",(self.record[j*5],self.record[j*5+1],self.record[j*5+2],self.record[j*5+3],self.record[j*5+4]))
				conn1.commit()
		finally:
			cur1.close()
			conn1.close()
		mainlayout=QHBoxLayout()
		mainlayout.addWidget(self.table)
		mainlayout.addWidget(self.button)
		self.setLayout(mainlayout)
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
	#	self.connect(self.button1,SIGNAL("clicked()",self.query))
		gridlayout=QGridLayout()
		gridlayout.addWidget(self.label1,0,0,1,2)
		gridlayout.addWidget(self.lineEdit1,0,2,1,1)
		gridlayout.addWidget(self.label2,0,3,1,2)
		gridlayout.addWidget(self.button1,1,4)
		gridlayout.addWidget(self.text1,2,0,1,5)
		mainlayout1=QHBoxLayout()
		mainlayout1.addLayout(gridlayout)
		self.setLayout(mainlayout1)
#	def qurey(self):
		
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
		mainlayout.addWidget(self.lineEdit1,2,1,1,2)
		mainlayout.addWidget(self.label4,3,0,)
		mainlayout.addWidget(self.lineEdit1,3,1,1,2)
		mainlayout.addWidget(self.label5,4,0,)
		mainlayout.addWidget(self.lineEdit1,4,1,1,2)
		mainlayout.addWidget(self.okbutton,5,1)
		self.addLayout(mainlayout)
		self.connect(self.okbutton,SIGNAL("clicked()"),self.update)
	def update(self):
		try:
			conn1=MySQLdb.connect(host='localhost',user='root',passwd='123456',db ='logindialog',charset='utf8')
			cur1=conn1.cursor()
			cur1.execute("insert into item value(%s,%s,%s,%s,%s)",(self.lineEdit1.text(),self.lineEdit2.text(),self.lineEdit3.text(),self.lineEdit4.text(),self.lineEdit5.text()))
		finally:
			cur1.close()
			conn1.close()
class MainWindow(QWidget):
	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		self.tab=QTabWidget()
		self.show=ShowItem()
		self.query=QueryItem()
		self.tab.addTab(self.show,"创建与修改".decode('utf-8'))
		self.tab.addTab(self.query,"查询".decode('utf-8'))
		mainlayout=QHBoxLayout()
		mainlayout.addWidget(self.tab)
		self.setLayout(mainlayout)
#app=QApplication(sys.argv)
#lll=mainwindow()
#lll.show()
#app.exec_()
