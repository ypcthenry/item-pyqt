#!/usr/bin/env python
# coding=utf-8
import sys
import con
import urllib2
from perfect import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
sys.path.append('home/thenry/code/pyqt')
class LoginDialog(QDialog):
	def __init__(self,parent=None):
		super(LoginDialog,self).__init__(parent)
		self.setWindowTitle('项目管理登录界面'.decode('utf8'))
		self.namelabel=QLabel('用户名 ：  '.decode('utf8'))
		self.namelineEdit=QLineEdit()
		self.namelabel.setBuddy(self.namelineEdit)
		self.passwdlabel=QLabel('密码 ：  '.decode('utf-8'))
		self.passwdlineEdit=QLineEdit()
		self.passwdlabel.setBuddy(self.passwdlineEdit)
		self.discardbutton=QPushButton('取消'.decode('utf-8'))
		self.loginbutton=QPushButton('登录'.decode('utf8'))
		self.loginbutton.setDefault(True)
		self.connect(self.discardbutton,SIGNAL("clicked()"),self.close)
		self.connect(self.loginbutton,SIGNAL("clicked()"),self.clicklogin)
		toplayout=QHBoxLayout()
		toplayout.addWidget(self.namelabel)
		toplayout.addWidget(self.namelineEdit)
		middlelayout=QHBoxLayout()
		middlelayout.addWidget(self.passwdlabel)
		middlelayout.addWidget(self.passwdlineEdit)
		bottomlayout=QHBoxLayout()
		bottomlayout.addWidget(self.discardbutton)
		bottomlayout.addWidget(self.loginbutton)
		mainlayout=QVBoxLayout()
		mainlayout.addLayout(toplayout)
		mainlayout.addLayout(middlelayout)
		mainlayout.addLayout(bottomlayout)
		self.setLayout(mainlayout)
	def clicklogin(self):
		textname=self.namelineEdit.text()
		textpasswd=self.passwdlineEdit.text()
		self.reject()
		for rec in con.allperson:
			if rec[1]==textname:
				if rec[2]==textpasswd:
					self.accept()
					self.close()
				else:
					QMessageBox.warning(self,'NOTICE','密码错误'.decode('utf-8'),QMessageBox.Close)
		if self.result()==QDialog.Rejected:
			QMessageBox.warning(self,'NOTICE','用户不存在'.decode('utf-8'),QMessageBox.Close)
app=QApplication(sys.argv)
loginDialog=LoginDialog()
if loginDialog.exec_()==QDialog.Rejected:
	sys.exit(1)
window=MainWindow()
window.show()
app.exec_()
