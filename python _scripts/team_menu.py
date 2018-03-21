# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_otherwindow(object):
    def setupUi(self, otherwindow):
        otherwindow.setObjectName("otherwindow")
        otherwindow.resize(277, 147)
        otherwindow.setStyleSheet("                        background-color: rgb(66,66,66);\n"
"")
        self.centralwidget = QtWidgets.QWidget(otherwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(50, 20, 191, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"                        background-color: rgb(66,66,66);\n"
"                    ")
        self.team_name.setObjectName("team_name")
        self.team_name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.team_name_text.setGeometry(QtCore.QRect(60, 50, 151, 31))
        self.team_name_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team_name_text.setObjectName("team_name_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 80, 23))
        self.pushButton.setStyleSheet("color:White\n"
"")
        self.pushButton.setObjectName("pushButton")
        otherwindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(otherwindow)
        QtCore.QMetaObject.connectSlotsByName(otherwindow)

    def retranslateUi(self, otherwindow):
        _translate = QtCore.QCoreApplication.translate
        otherwindow.setWindowTitle(_translate("otherwindow", "MainWindow"))
        self.team_name.setText(_translate("otherwindow", "Enter The Team Name"))
        self.pushButton.setText(_translate("otherwindow", "Save"))

