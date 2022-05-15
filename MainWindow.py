# -*- coding: utf-8 -*-
import time

from PyQt5.QtCore import Qt, QPoint, QThread, QMutex
from PyQt5.QtGui import QMouseEvent, QMovie
from win32ctypes.core import ctypes

import resources_rc
import settingWindow, data, login_ruijie
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

"""
当前问题，显示提示窗时不能关闭当前函数，从提示窗返回函数时，属于开启新的窗口，
无法显示原来的窗口

"""
    # 继承QThread
class Thread_1(QThread):  # 线程1
    def __init__(self):
        super().__init__()

    def run(self):
        # qmut_1 = QMutex()  # 创建线程锁
        while (True):
            # self.qmut_1.lock()  # 加锁
            print(login_ruijie.sing_log())
            time.sleep(2)  # 休眠
            if login_ruijie.sing_log() != 2:
                # window.hide()
                try:
                    # window.th.finished()
                    # ret = ctypes.windll.kernel32.TerminateThread(self._thread.handle, 0)
                    # print('终止线程', self._thread.handle, ret)
                    print("关闭线程")
                except:
                    print("线程未启动")

            # self.qmut_1.unlock()  # 解锁
                window.pushButton_login.show()


class Ui_MainWindow(QMainWindow):

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

    def setting_click(self):
        self.hide()
        self.set_win = settingWindow.SettingWindow()
        self.set_win.show()

    def button_click(self):

        self.pushButton_login.hide()
        self.gif = QMovie(":/image/resource/dialog.gif")
        self.gif.setScaledSize(self.dialog.size())
        self.dialog.setMovie(self.gif)
        self.gif.start()
        print("点击了登录")  # 这里为按键的监听函数，所以需要在程序初始化时就检查是否已经存在账号和密码
        self.getUsearName = self.lineEditUser.text()
        self.getUsearPassword = self.lineEditPassword.text()
        data.write_data("User_information",
                        self.getUsearName + "\n" + self.getUsearPassword + "\n" + str(self.checkBox.isChecked()), 'w')
        """
        判断txt中是否有账户和密码，有则读取，无则可以写入
        将账号和密码写入txt
        读取txt中的账号与密码
        显示在输入框
        """
        print(self.getUsearName)
        print(self.getUsearPassword)
        # 调用call_func 传值和开启新线程
        login_ruijie.call_func(self.getUsearName, self.getUsearPassword)
        self.start_thread()

        # @staticmethod

    def slot_check_box(self):
        # 　判断是否选中
        check_box_status = self.checkBox.isChecked()
        print("被点击了")
        self.checkBox.setChecked(check_box_status)
        self.getUsearName = self.lineEditUser.text()
        self.getUsearPassword = self.lineEditPassword.text()
        data.write_data("User_information",
                        self.getUsearName + "\n" + self.getUsearPassword + "\n" + str(self.checkBox.isChecked()), 'w')
        print("checkBox:" + str(check_box_status))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 260, 380))
        self.background.setStyleSheet("background-color: rgb(125, 200, 158);\n"
                                      "border-radius:20px;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(30, 280, 200, 40))
        self.pushButton_login.setStyleSheet(
            "#pushButton_login{\n"
            "color: rgb(255, 255, 255);\n"
            "background-color:rgb(82, 156, 113);\n"
            "border-radius:20px;\n"
            "font: 16pt \"SentyTEA 新蒂下午茶体\";\n"
            "}\n"

            "#pushButton_login:hover{\n"
            "background-color:rgb(108, 206, 149);\n"
            "}\n"

            "#pushButton_login:pressed\n"
            "{\n"
            "background-color:rgb(69, 131, 95);\n"
            "padding-left:3px;\n"
            "padding-top:3px;\n"
            "}\n"
            "")
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEditUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUser.setGeometry(QtCore.QRect(60, 161, 160, 30))
        self.lineEditUser.setStyleSheet("border-radius:1px;\n"
                                        "font: 9pt \"01FLOPDESIGN\";\n"
                                        "color:rgb(59, 118, 87);")
        self.lineEditUser.setText("")
        self.lineEditUser.setObjectName("lineEditUser")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(60, 212, 160, 30))
        self.lineEditPassword.setStyleSheet("border-radius:1px;\n"
                                            "font: 9pt \"01FLOPDESIGN\";\n"
                                            "color:rgb(59, 118, 87);")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.edit_background_1 = QtWidgets.QLabel(self.centralwidget)
        self.edit_background_1.setGeometry(QtCore.QRect(30, 160, 200, 32))
        self.edit_background_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius:15px")
        self.edit_background_1.setText("")
        self.edit_background_1.setObjectName("edit_background_1")
        self.edit_background_2 = QtWidgets.QLabel(self.centralwidget)
        self.edit_background_2.setGeometry(QtCore.QRect(30, 210, 200, 32))
        self.edit_background_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius:15px")
        self.edit_background_2.setText("")
        self.edit_background_2.setObjectName("edit_background_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 250, 111, 18))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        # 点击事件
        self.checkBox.clicked.connect(self.slot_check_box)
        user = ""
        password = ""
        try:
            if data.read_date("User_information")[2] == "True":
                user = data.read_date("User_information")[0].split("\n")[0]
                password = data.read_date("User_information")[1].split("\n")[0]
                print(data.read_date("User_information"))
                self.checkBox.setChecked(True)
        except:
            pass

        self.lineEditUser.setText(user)
        self.lineEditPassword.setText(password)
        print(user)
        print("----------------")
        print(password)
        print("----------------")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 100, 100))
        self.label.setStyleSheet("background-image: url(:/image/resource/头像（1）.png);")
        self.label.setText("")
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(36, 164, 20, 20))
        self.label_2.setStyleSheet("image: url(:/image/resource/头像.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(36, 216, 20, 20))
        self.label_3.setStyleSheet("image: url(:/image/resource/钥匙.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Exit0 = QtWidgets.QPushButton(self.centralwidget)
        self.Exit0.setGeometry(QtCore.QRect(223, 10, 26, 26))
        self.Exit0.setStyleSheet("border-radius:10px;\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "font: 9pt \"01FLOPDESIGN\";")
        self.Exit0.setObjectName("Exit0")

        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(20, 340, 23, 23))
        self.help_button.setStyleSheet("QPushButton{\n"
                                       "border-radius:10px;\n"
                                       "background-image: url(:/image/resource/帮助未按下.png);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "    background-image: url(:/image/resource/帮助按下.png);\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed{\n"
                                       "    padding-left:3px;\n"
                                       "    padding-top:3px;\n"
                                       "}\n"
                                       "")
        self.help_button.setText("")
        self.help_button.setObjectName("help_button")

        self.help_button.clicked.connect(self.start_thread)

        self.setting_button = QtWidgets.QPushButton(self.centralwidget)
        self.setting_button.setGeometry(QtCore.QRect(215, 335, 28, 28))
        self.setting_button.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "border-radius:10px;\n"
                                          "background-image: url(:/image/resource/设置未按下.png);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover\n"
                                          "{\n"
                                          "    \n"
                                          "    background-image: url(:/image/resource/设置按下.png);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed\n"
                                          "{\n"
                                          "    padding-left:3px;\n"
                                          "    padding-top:3px;\n"
                                          "}\n"
                                          "")
        self.setting_button.setText("")
        self.setting_button.setObjectName("setting_button")

        self.pushButton_login.clicked.connect(self.button_click)  # 点击登录按键响应
        self.setting_button.clicked.connect(self.setting_click)  # 打开设置窗口

        self.dialog = QtWidgets.QLabel(self.centralwidget)
        self.dialog.setGeometry(QtCore.QRect(30, 280, 200, 40))
        # self.dialog.setStyleSheet("border-radius:20px;")



        # self.background.raise_()

        # self.edit_background_2.raise_()
        # self.edit_background_1.raise_()
        self.lineEditUser.raise_()
        self.lineEditPassword.raise_()
        # self.label.raise_()
        # self.label_2.raise_()
        # self.label_3.raise_()
        # self.Exit0.raise_()
        # self.checkBox.raise_()
        # self.help_button.raise_()
        # self.setting_button.raise_()

        self.dialog.raise_()

        self.pushButton_login.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Exit0.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.lineEditUser.setPlaceholderText(_translate("MainWindow", "user"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "password"))
        self.Exit0.setText(_translate("MainWindow", "X"))
        self.checkBox.setText(_translate("MainWindow", "记住账号密码"))


    def start_thread(self):
        self.th = Thread_1()
        self.th.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()  # MainWindow1随便改
    window.show()
    sys.exit(app.exec_())
