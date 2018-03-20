# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saved_teams.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(274, 482)
        MainWindow.setStyleSheet("                        background-color: rgb(66,66,66);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color : white\n"
"")
        self.label.setObjectName("label")
        self.saved_teams_list = QtWidgets.QListView(self.centralwidget)
        self.saved_teams_list.setGeometry(QtCore.QRect(10, 40, 256, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saved_teams_list.setFont(font)
        self.saved_teams_list.setStyleSheet("background-color : white")
        self.saved_teams_list.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.saved_teams_list.setAlternatingRowColors(False)
        self.saved_teams_list.setObjectName("saved_teams_list")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(100, 430, 80, 23))
        self.open_button.setStyleSheet("color: white        ")
        self.open_button.setObjectName("open_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SAVED TEAMS"))
        self.open_button.setText(_translate("MainWindow", "OPEN"))

