# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team_saved_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_team_saved_dialog(object):
    def setupUi(self, team_saved_dialog):
        team_saved_dialog.setObjectName("team_saved_dialog")
        team_saved_dialog.resize(337, 126)
        team_saved_dialog.setStyleSheet("background-color: rgb(239, 83, 80);\n"
"                        background-color: rgb(66,66,66);\n"
"            ")
        self.centralwidget = QtWidgets.QWidget(team_saved_dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.team_save_dialog_btn = QtWidgets.QPushButton(self.centralwidget)
        self.team_save_dialog_btn.setGeometry(QtCore.QRect(130, 80, 80, 23))
        self.team_save_dialog_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.team_save_dialog_btn.setObjectName("team_save_dialog_btn")
        team_saved_dialog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(team_saved_dialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 20))
        self.menubar.setObjectName("menubar")
        team_saved_dialog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(team_saved_dialog)
        self.statusbar.setObjectName("statusbar")
        team_saved_dialog.setStatusBar(self.statusbar)

        self.retranslateUi(team_saved_dialog)
        QtCore.QMetaObject.connectSlotsByName(team_saved_dialog)

    def retranslateUi(self, team_saved_dialog):
        _translate = QtCore.QCoreApplication.translate
        team_saved_dialog.setWindowTitle(_translate("team_saved_dialog", "MainWindow"))
        self.label.setText(_translate("team_saved_dialog", "YOUR TEAM HAS BEEN SAVED!"))
        self.team_save_dialog_btn.setText(_translate("team_saved_dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    team_saved_dialog = QtWidgets.QMainWindow()
    ui = Ui_team_saved_dialog()
    ui.setupUi(team_saved_dialog)
    team_saved_dialog.show()
    sys.exit(app.exec_())

