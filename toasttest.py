# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toasttest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToastWindow(object):
    def setupUi(self, ToastWindow):
        ToastWindow.setObjectName("ToastWindow")
        ToastWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        ToastWindow.resize(400, 150)
        ToastWindow.setWindowTitle("MainWindow")
        ToastWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        ToastWindow.setAnimated(False)
        ToastWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        ToastWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(ToastWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 120, 400, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(140, 198, 255, 201), stop:0.767568 rgba(255, 255, 255, 110));\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(18)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 0, 30, 30))
        self.pushButton.setStyleSheet("font: 9pt \"01FLOPDESIGN\";\n"
"color: rgb(107, 107, 107);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        ToastWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ToastWindow)
        QtCore.QMetaObject.connectSlotsByName(ToastWindow)

    def retranslateUi(self, ToastWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("ToastWindow", "toastText"))
        self.pushButton.setText(_translate("ToastWindow", "X"))