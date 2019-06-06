# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 798)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.MsgTE = QtWidgets.QTextEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.MsgTE.setFont(font)
        self.MsgTE.setReadOnly(True)
        self.MsgTE.setObjectName("MsgTE")
        self.gridLayout_4.addWidget(self.MsgTE, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 3, 0, 1, 2)
        self.DispFm = QtWidgets.QFrame(self.frame)
        self.DispFm.setMaximumSize(QtCore.QSize(16777215, 598))
        self.DispFm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DispFm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DispFm.setObjectName("DispFm")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.DispFm)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DiscernBt = QtWidgets.QPushButton(self.DispFm)
        self.DiscernBt.setObjectName("DiscernBt")
        self.gridLayout_3.addWidget(self.DiscernBt, 0, 4, 1, 1)
        self.StopBt = QtWidgets.QPushButton(self.DispFm)
        self.StopBt.setObjectName("StopBt")
        self.gridLayout_3.addWidget(self.StopBt, 0, 1, 1, 1)
        self.ShowBt = QtWidgets.QPushButton(self.DispFm)
        self.ShowBt.setObjectName("ShowBt")
        self.gridLayout_3.addWidget(self.ShowBt, 0, 0, 1, 1)
        self.ExitBt = QtWidgets.QPushButton(self.DispFm)
        self.ExitBt.setObjectName("ExitBt")
        self.gridLayout_3.addWidget(self.ExitBt, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.DispFm)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(False)
        self.label.setAcceptDrops(False)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 2)
        self.DispLb = QtWidgets.QLabel(self.DispFm)
        self.DispLb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DispLb.setText("")
        self.DispLb.setObjectName("DispLb")
        self.gridLayout_3.addWidget(self.DispLb, 1, 1, 1, 4)
        self.gridLayout_2.addWidget(self.DispFm, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MsgTE.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">欢迎使用</p></body></html>"))
        self.DiscernBt.setText(_translate("MainWindow", "开始识别"))
        self.StopBt.setText(_translate("MainWindow", "暂停"))
        self.ShowBt.setText(_translate("MainWindow", "打开摄像头"))
        self.ExitBt.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">人脸识别签到系统</p></body></html>"))

