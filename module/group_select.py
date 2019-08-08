# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Form implementation generated from reading ui file 'document_up_down.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from _socket import socket

from PyQt5 import QtCore, QtGui, QtWidgets

# from xiazai import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog


class Ui_Group(QtWidgets.QMainWindow):

    def __init__(self, my_info, s):
        super().__init__()
        self.setupUi(self)
        self.my_info = my_info
        self.s = s
        self.tx = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(255, 80, 50, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.findgroup)

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(300, 80, 50, 30))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.clicked.connect(self.delgroup)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(210, 25, 70, 30))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.build)

        self.txbutton = QtWidgets.QPushButton(self.centralwidget)
        self.txbutton.setGeometry(QtCore.QRect(80, 15, 80, 50))
        self.txbutton.setText("")
        self.txbutton.setObjectName("txbutton")
        path = './avatar0.jpg'
        self.txbutton.setStyleSheet("border-image:url(%s)" % path)
        self.txbutton.clicked.connect(self.test1)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 321, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit.setPlaceholderText("请输入群号/群名")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # 选择图像
    def test1(self):
        openfile_name = QFileDialog.getOpenFileName(self)
        # print(openfile_name)
        path = openfile_name[0]
        self.tx = path
        print(path)
        # yzbtun
        self.txbutton.setStyleSheet("border-image:url(%s)" % path)


    def recvinfo(self,data):
        if data == "nois":
            self.textBrowser.append("此群不存在")
        elif data == "havebeen":
            self.textBrowser.append("已在此群")
        else:
            self.textBrowser.append("加群成功")

    def recvinfo1(self,data):
        if data == "nois":
            self.textBrowser.append('此群不存在')
        elif data == "not":
            self.textBrowser.append("不在此群")
        else:
            self.textBrowser.append("退群成功")

    def recvinfo2(self,data):
        if data == "nois":
            self.textBrowser.append('已超过创建数量限制')
        elif data == "not":
            self.textBrowser.append("创建失败")
        else:
            self.textBrowser.append("群组创建成功,群号:"+data)

    def findgroup(self):
        self.textBrowser.clear()
        ID_GRO = self.lineEdit.text()
        self.s.send(("U"+ " " + self.my_info["rootname"] + " " + ID_GRO).encode())

    def delgroup(self):
        self.textBrowser.clear()
        ID_GRO = self.lineEdit.text()
        self.s.send(("B"+ " " + self.my_info["rootname"] + " " + ID_GRO).encode())

    def build(self):
        self.textBrowser.clear()
        name_GRO = self.lineEdit.text()
        self.s.send(("N"+ " " + self.my_info["rootname"]+ " " + name_GRO + " " + self.tx).encode())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "加群"))
        self.pushButton1.setText(_translate("MainWindow", "退群"))
        self.pushButton2.setText(_translate("MainWindow", "创建群组"))
