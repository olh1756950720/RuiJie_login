# -*- coding: utf-8 -*-
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def sleep(h = 0, m = 0, t = 0):
    def sleeptime(hour, min, sec):
        """延时函数"""
        return hour * 3600 + min * 60 + sec
        # time.sleep(sleeping(0, 0, 5)) 调用方式
    time.sleep(sleeptime(h, m, t))

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 120, 260, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(
        "color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(140, 198, 255, 201), stop:0.767568 rgba(255, 255, 255, 0));\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label.setIndent(18)
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(0, 120, 260, 30))
        self.button_close.setStyleSheet("font: 9pt \"01FLOPDESIGN\";\n"
                                      "color: rgb(107, 107, 107);\n"
                                      "background-color: rgba(255, 255, 255, 0);")
        self.button_close.setObjectName("button_close")
        self.button_close.clicked.connect(self.close)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "toastText"))
        self.button_close.setText(_translate("ToastWindow", ""))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = Ui_MainWindow()
    window1.show()
    sys.exit(app.exec_())

