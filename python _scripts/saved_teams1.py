# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saved_windows(object):
    def setupUi(self, saved_windows):
        saved_windows.setObjectName("saved_windows")
        saved_windows.resize(274, 482)
        saved_windows.setStyleSheet("                        background-color: rgb(66,66,66);\n"
"")
        self.centralwidget = QtWidgets.QWidget(saved_windows)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color : white\n"
"")
        self.label.setObjectName("label")
        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setGeometry(QtCore.QRect(100, 430, 80, 23))
        self.open_button.setStyleSheet("color: white        ")
        self.open_button.setObjectName("open_button")
        self.saved_windows_table = QtWidgets.QTableWidget(self.centralwidget)
        self.saved_windows_table.setGeometry(QtCore.QRect(10, 30, 256, 391))
        self.saved_windows_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.saved_windows_table.setObjectName("saved_windows_table")
        self.saved_windows_table.setColumnCount(0)
        self.saved_windows_table.setRowCount(0)
        saved_windows.setCentralWidget(self.centralwidget)

        self.retranslateUi(saved_windows)
        QtCore.QMetaObject.connectSlotsByName(saved_windows)

    def retranslateUi(self, saved_windows):
        _translate = QtCore.QCoreApplication.translate
        saved_windows.setWindowTitle(_translate("saved_windows", "MainWindow"))
        self.label.setText(_translate("saved_windows", "SAVED TEAMS"))
        self.open_button.setText(_translate("saved_windows", "OPEN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saved_windows = QtWidgets.QMainWindow()
    ui = Ui_saved_windows()
    ui.setupUi(saved_windows)
    saved_windows.show()
    sys.exit(app.exec_())

