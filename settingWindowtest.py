# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingWindowtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(20, 10, 260, 380))
        self.background.setStyleSheet("background-color: rgb(125, 200, 158);\n"
"border-radius:20px;")
        self.background.setText("")
        self.background.setObjectName("background")
        self.Exit1 = QtWidgets.QPushButton(self.centralwidget)
        self.Exit1.setGeometry(QtCore.QRect(243, 30, 26, 26))
        self.Exit1.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"01FLOPDESIGN\";")
        self.Exit1.setObjectName("Exit1")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(33, 30, 26, 26))
        self.back.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"01FLOPDESIGN\";")
        self.back.setObjectName("back")
        self.back.clicked.connect(self.backView)  # 返回按键点击事件

        self.file_adress_buttton = QtWidgets.QPushButton(self.centralwidget)
        self.file_adress_buttton.setGeometry(QtCore.QRect(40, 290, 221, 40))
        self.file_adress_buttton.setStyleSheet("background-color:rgb(82, 156, 113);\n"
"border-radius:10px;\n"
"font:12pt \"等线\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.file_adress_buttton.setObjectName("file_adress_buttton")
        self.file_adress_buttton.clicked.connect(self.getfile)  # 获取文件地址

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 250, 221, 31))
        self.textBrowser.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(252, 252, 252);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText(data.read_date("file_adress")[0])  # 设置文字内容

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 340, 101, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"等线\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 360, 101, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"等线\";")
        self.label_2.setObjectName("label_2")
        self.student_name = QtWidgets.QLineEdit(self.centralwidget)
        self.student_name.setGeometry(QtCore.QRect(100, 80, 160, 30))
        self.student_name.setStyleSheet("border-radius:10px;\n"
"font: 9pt \"01FLOPDESIGN\";\n"
"color:rgb(59, 118, 87);")
        self.student_name.setText("")
        self.student_name.setPlaceholderText("")
        self.student_name.setObjectName("student_name")
        self.stu_number = QtWidgets.QLineEdit(self.centralwidget)
        self.stu_number.setGeometry(QtCore.QRect(100, 120, 160, 30))
        self.stu_number.setStyleSheet("border-radius:10px;\n"
"font: 9pt \"01FLOPDESIGN\";\n"
"color:rgb(59, 118, 87);")
        self.stu_number.setText("")
        self.stu_number.setPlaceholderText("")
        self.stu_number.setObjectName("stu_number")
        self.stu_password = QtWidgets.QLineEdit(self.centralwidget)
        self.stu_password.setGeometry(QtCore.QRect(100, 160, 160, 30))
        self.stu_password.setStyleSheet("border-radius:10px;\n"
"font: 9pt \"01FLOPDESIGN\";\n"
"color:rgb(59, 118, 87);")
        self.stu_password.setText("")
        self.stu_password.setPlaceholderText("")
        self.stu_password.setObjectName("stu_password")
        self.school_code = QtWidgets.QLineEdit(self.centralwidget)
        self.school_code.setGeometry(QtCore.QRect(100, 200, 160, 30))
        self.school_code.setStyleSheet("border-radius:10px;\n"
"font: 9pt \"01FLOPDESIGN\";\n"
"color:rgb(59, 118, 87);")
        self.school_code.setText("")
        self.school_code.setPlaceholderText("")
        self.school_code.setObjectName("school_code")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 87, 41, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"等线\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 127, 41, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"等线\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 167, 41, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"等线\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(27, 207, 71, 16))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"等线\";")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Exit1.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Exit1.setText(_translate("MainWindow", "X"))
        self.back.setText(_translate("MainWindow", "<-"))
        self.file_adress_buttton.setText(_translate("MainWindow", "文件目录"))
        self.label.setText(_translate("MainWindow", "作者：欧小红"))
        self.label_2.setText(_translate("MainWindow", "2022年5月14日"))
        self.label_3.setText(_translate("MainWindow", "姓名"))
        self.label_4.setText(_translate("MainWindow", "学号"))
        self.label_5.setText(_translate("MainWindow", "密码"))
        self.label_6.setText(_translate("MainWindow", "学校编号"))
import resource_rc
