import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import resource_rc
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent


class Stats(QMainWindow):

    def __init__(self):

        # 从文件中加载UI定义
        self.ui = uic.loadUi("MainWindow.ui")
        self.ui.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        self.ui.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        # 重写移动事件


    def mouseMoveEvent(self, e: QMouseEvent):
        if self.ui._tracking:
            self.ui._endPos = e.pos() - self.ui._startPos
            self.ui.move(self.ui.pos() + self.ui._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.ui._startPos = QPoint(e.x(), e.y())
            self.ui._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.ui._tracking = False
            self.ui._startPos = None
            self.ui._endPos = None


def btn_click():
    print("你点击了按钮")


if __name__ == "__main__":
    App = QApplication(sys.argv)  # 创建QApplication对象，作为GUI主程序入口
    stats = Stats()
    stats.ui.show()  # 显示主窗体
    stats.ui.pushButton_login.clicked.connect(btn_click)
    sys.exit(App.exec_())   # 循环中等待退出程序

