# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QMovie

import MainWindow
import MainWindow as MW
import data
import login_ruijie
import resources_rc
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Fail_Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明

        # 重写移动事件

    def mouseMoveEvent(self, e: QMouseEvent):
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    def backView(self):
        self.hide()
        self.mainWindow = MainWindow.Ui_MainWindow()
        self.mainWindow.show()

    def try_again(self):
        user = data.read_date("User_information")[0].split("\n")[0]
        password = data.read_date("User_information")[1].split("\n")[0]
        login_ruijie.call_func(user, password)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 260, 220))
        self.background.setStyleSheet("background-color: rgb(110, 176, 138);\n"
"border-radius:20px;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(223, 10, 26, 26))
        self.Exit.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"01FLOPDESIGN\";")
        self.Exit.setObjectName("Exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 50, 50))
        # self.label.setText("")
        # self.label.setObjectName("label")
        self.gif = QMovie(":/image/resource/fail.gif")
        self.gif.setScaledSize(self.label.size())
        self.label.setMovie(self.gif)
        self.gif.start()
        self.pushButton_fail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fail.setGeometry(QtCore.QRect(30, 160, 200, 40))
        self.pushButton_fail.setStyleSheet("#pushButton_fail{\n"
"    selection-color: rgb(0, 170, 127);\n"
"    background-color:rgb(82, 156, 113);\n"
"    border-radius:20px;\n"
"    font: 16pt \"幼圆\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_fail{\n"
"    padding_top:20px;\n"
"}\n"
"#pushButton_fail:pressed\n"
"{\n"
"background-color:rgb(69, 131, 95);\n"
"padding-left:3px;\n"
"padding-top:3px;\n"
"}")
        self.pushButton_fail.setObjectName("pushButton_fail")

        # self.pushButton_fail.clicked.connect(self.try_again)
        self.pushButton_fail.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Exit.setText(_translate("MainWindow", "X"))
        self.pushButton_fail.setText(_translate("MainWindow", "重试"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Fail_Window()  # MainWindow1随便改
    mainWindow.show()
    sys.exit(app.exec_())


