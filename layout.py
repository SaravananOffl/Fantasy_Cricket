# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 566)
        MainWindow.setStyleSheet("background-color: rgb(239, 83, 80);\n"
                                 "background-color: rgb(41, 182, 246);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(20, 50, 661, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.columnView.setFont(font)
        self.columnView.setStyleSheet("background-color: rgb(63, 81, 181);")
        self.columnView.setObjectName("columnView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 112, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(63, 81, 181);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 60, 113, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(63, 81, 181);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 60, 150, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(63, 81, 181);")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 60, 123, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(63, 81, 181);")
        self.label_4.setObjectName("label_4")
        self.db_list = QtWidgets.QListView(self.centralwidget)
        self.db_list.setGeometry(QtCore.QRect(20, 150, 281, 361))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.db_list.setFont(font)
        self.db_list.setStyleSheet("border-color: rgb(191, 54, 12);\n"
                                   "background-color: rgb(63, 81, 181);\n"
                                   "border-top-color: rgb(255, 255, 255);")
        self.db_list.setObjectName("db_list")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(400, 150, 281, 361))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listView_2.setFont(font)
        self.listView_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(63, 81, 181);")
        self.listView_2.setObjectName("listView_2")
        self.move_btn = QtWidgets.QPushButton(self.centralwidget)
        self.move_btn.setGeometry(QtCore.QRect(310, 300, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.move_btn.setFont(font)
        self.move_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(26, 35, 126);\n"
                                    "border-color: rgb(255, 255, 255);")
        self.move_btn.setObjectName("move_btn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 130, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.bow_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.bow_radio.setGeometry(QtCore.QRect(102, 158, 59, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bow_radio.setFont(font)
        self.bow_radio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(63, 81, 181);")
        self.bow_radio.setObjectName("bow_radio")
        self.ar_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.ar_radio.setGeometry(QtCore.QRect(167, 158, 46, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ar_radio.setFont(font)
        self.ar_radio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(63, 81, 181);\n"
                                    "")
        self.ar_radio.setObjectName("ar_radio")
        self.wk_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.wk_radio.setGeometry(QtCore.QRect(219, 158, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.wk_radio.setFont(font)
        self.wk_radio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(63, 81, 181);\n"
                                    "")
        self.wk_radio.setObjectName("wk_radio")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(20, 190, 281, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listView_3.setFont(font)
        self.listView_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listView_3.setObjectName("listView_3")
        self.team_list = QtWidgets.QListView(self.centralwidget)
        self.team_list.setGeometry(QtCore.QRect(400, 190, 281, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.team_list.setFont(font)
        self.team_list.setStyleSheet("border-color: rgb(85, 255, 127);\n"
                                     "background-color: rgb(255, 255, 255);")
        self.team_list.setObjectName("team_list")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(411, 161, 113, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(63, 81, 181);\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.no_bat = QtWidgets.QLabel(self.centralwidget)
        self.no_bat.setGeometry(QtCore.QRect(160, 60, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.no_bat.setFont(font)
        self.no_bat.setStyleSheet("color: rgb(255, 255, 255)\n"
                                  ";background-color: rgb(63, 81, 181);")
        self.no_bat.setObjectName("no_bat")
        self.bat_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_radio.setGeometry(QtCore.QRect(41, 158, 55, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bat_radio.setFont(font)
        self.bat_radio.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bat_radio.setAcceptDrops(False)
        self.bat_radio.setToolTipDuration(-3)
        self.bat_radio.setAutoFillBackground(False)
        self.bat_radio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(63, 81, 181);")
        self.bat_radio.setCheckable(True)
        self.bat_radio.setChecked(False)
        self.bat_radio.setObjectName("bat_radio")
        self.no_ar = QtWidgets.QLabel(self.centralwidget)
        self.no_ar.setGeometry(QtCore.QRect(460, 60, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.no_ar.setFont(font)
        self.no_ar.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(63, 81, 181);")
        self.no_ar.setObjectName("no_ar")
        self.no_bow = QtWidgets.QLabel(self.centralwidget)
        self.no_bow.setGeometry(QtCore.QRect(310, 60, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.no_bow.setFont(font)
        self.no_bow.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(63, 81, 181);")
        self.no_bow.setObjectName("no_bow")
        self.no_wk = QtWidgets.QLabel(self.centralwidget)
        self.no_wk.setGeometry(QtCore.QRect(640, 60, 16, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.no_wk.setFont(font)
        self.no_wk.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(63, 81, 181);")
        self.no_wk.setObjectName("no_wk")
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(530, 161, 50, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(63, 81, 181);\n"
                                     "")
        self.team_name.setObjectName("team_name")
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(520, 130, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.points_used.setFont(font)
        self.points_used.setStyleSheet("color: rgb(255, 255, 255);")
        self.points_used.setObjectName("points_used")
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setGeometry(QtCore.QRect(180, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setStyleSheet("color: rgb(255, 255, 255);")
        self.points_available.setObjectName("points_available")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 20))
        self.menubar.setStyleSheet("background-color: rgb(66,66,66);\n"
                                   "color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(66,66,66);")
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_team = QtWidgets.QAction(MainWindow)
        self.actionNEW_team.setVisible(True)
        self.actionNEW_team.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionNEW_team.setObjectName("actionNEW_team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Teams.addAction(self.actionNEW_team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections :"))
        self.label_2.setText(_translate("MainWindow", "Batsmen(BAT) "))
        self.label_3.setText(_translate("MainWindow", "Bowlers(BOW) "))
        self.label_5.setText(_translate("MainWindow", "Wicket-Keeper(WK) "))
        self.label_4.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.move_btn.setText(_translate("MainWindow", ">"))
        self.label_6.setText(_translate("MainWindow", "PoInts Available :"))
        self.label_7.setText(_translate("MainWindow", "Points Used :"))
        self.bow_radio.setText(_translate("MainWindow", "BOW"))
        self.ar_radio.setText(_translate("MainWindow", "AR"))
        self.wk_radio.setText(_translate("MainWindow", "WK"))
        self.label_8.setText(_translate("MainWindow", "TEAM NAME :"))
        self.no_bat.setText(_translate("MainWindow", "0"))
        self.bat_radio.setText(_translate("MainWindow", "BAT"))
        self.no_ar.setText(_translate("MainWindow", "0"))
        self.no_bow.setText(_translate("MainWindow", "0"))
        self.no_wk.setText(_translate("MainWindow", "0"))
        self.team_name.setText(_translate("MainWindow", "NAME"))
        self.points_used.setText(_translate("MainWindow", "0"))
        self.points_available.setText(_translate("MainWindow", "0"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "EVALUATE Team"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
