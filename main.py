# -*- coding: utf-8 -*-
import time

from PyQt5.QtWidgets import QApplication

import login_finish
import toast, sys

def sleep(h = 0, m = 0, t = 0):
    def sleeptime(hour, min, sec):
        """延时函数"""
        return hour * 3600 + min * 60 + sec
        # time.sleep(sleeping(0, 0, 5)) 调用方式
    time.sleep(sleeptime(h, m, t))

def show_window():
    app = QApplication(sys.argv)
    finish_messageBox = login_finish.Finish_Window()
    finish_messageBox.show()
    sys.exit(app.exec_())  # 执行到这里的时候，窗口才会正在显示，并且就会停止执行下面的代码，并循环等待事件，知道程序退出



show_window()
