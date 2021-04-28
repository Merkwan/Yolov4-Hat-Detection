# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(170, 10, 730, 100))
        self.title.setText("")
        self.title.setObjectName("title")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 170, 131, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openCv = QtWidgets.QPushButton(self.layoutWidget)
        self.openCv.setObjectName("openCv")
        self.verticalLayout.addWidget(self.openCv)
        self.openVt = QtWidgets.QPushButton(self.layoutWidget)
        self.openVt.setObjectName("openVt")
        self.verticalLayout.addWidget(self.openVt)
        self.openPt = QtWidgets.QPushButton(self.layoutWidget)
        self.openPt.setObjectName("openPt")
        self.verticalLayout.addWidget(self.openPt)
        self.Open = QtWidgets.QPushButton(self.layoutWidget)
        self.Open.setObjectName("Open")
        self.verticalLayout.addWidget(self.Open)
        self.openPic = QtWidgets.QPushButton(self.layoutWidget)
        self.openPic.setObjectName("openPic")
        self.verticalLayout.addWidget(self.openPic)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1088, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主界面"))
        self.openCv.setText(_translate("MainWindow", "打开摄像头检测"))
        self.openVt.setText(_translate("MainWindow", "打开视频检测"))
        self.openPt.setText(_translate("MainWindow", "打开图片检测"))
        self.Open.setText(_translate("MainWindow", "视频检测结果展示"))
        self.openPic.setText(_translate("MainWindow", "图片检测结果展示"))
