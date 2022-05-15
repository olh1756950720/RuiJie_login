# -*- coding:utf-8 -*-
import os
import sys
import time
import threading

from PyQt5.QtWidgets import QApplication

import MainWindow as MW
import data
import login_fail
import login_finish
import weiShao_checkIn as wCK
signLog = 2
key = 0
state = 0

def detectionNetwork():
    """检查当前网络状态返回一个是否连接成功"""

    print("进入ping方法")
    pin = os.system('ping 8.8.8.8')
    print(pin)
    return pin

def sleep(h = 0, m = 0, t = 0):
    def sleeptime(hour, min, sec):
        """延时函数"""
        return hour * 3600 + min * 60 + sec
        # time.sleep(sleeptime(0, 0, 5)) 调用方式
    time.sleep(sleeptime(h, m, t))
def getpopen(result):
    """取得popen文本并输出"""
    strget = ""
    i = 0
    for line in result.readlines():
        print("%d: " % i + line)
        i = i + 1
        strget += line
    return strget
def findtxt(var, strget):
    """查找文本"""
    if var in strget:
        s = 1
    else:
        s = 0
    if s == 1:
        print("返回结果 = %s" % var)
    return s

def call_signIn(func, id, password):
    """signIn()的回调函数"""
    t = threading.Thread(target=func, args=(id, password, ))
    t.start()
    pass

def call_func(id, password):
    call_signIn(signIn, id, password)

def finish_window():
    app = QApplication(sys.argv)
    finish_messageBox = login_finish.Finish_Window()
    finish_messageBox.show()
    sys.exit(app.exec_())  # 执行到这里的时候，窗口才会正在显示，并且就会停止执行下面的代码，并循环等待事件，知道程序退出

def fail_window():
    app = QApplication(sys.argv)
    fail_messageBox = login_fail.Fail_Window()
    fail_messageBox.show()
    sys.exit(app.exec_())  # 执行到这里的时候，窗口才会正在显示，并且就会停止执行下面的代码，并循环等待事件，知道程序退出

def signIn(id, password):
    """登录方法"""

    print("进入登录方法")
    print("关闭锐捷")
    global signLog
    signLog = 2
    closeR = os.popen('taskkill /f /t /im 8021x.exe')
    strget = getpopen(closeR)
    print(strget)
    sleep(t=2)

    print("打开锐捷")
    file_adress = data.read_date("file_adress")[0].split("\n")[0]
    startR = os.popen(file_adress)
    # startR = os.popen('D:\8021x.lnk')#
    strget = getpopen(startR)
    print(strget)
    sleep(t=2)

    print("开始连接宽带")
    com = '@Rasdial 宽带连接 '
    com = com + id + ' ' + password

    print("开始连接宽带")
    result = os.popen(com)
    strget = getpopen(result)
    print(strget)

    var = "访问错误"

    signLog = 2
    signLog = findtxt(var, strget)  # 找到就返回1，否则为0
    if signLog == 0:
        print("链接成功")
        wCK.loging()  # 登录微哨
        wCK.run()  # 尝试进行打卡
        finish_window()
    elif signLog == 1:
        print("链接失败")
        fail_window()

def sing_log():
    return signLog




