#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 9:39
# @Author  : tanxw
# @Desc    : gui程序设计-第一个gui面世
"""
GUI(Graphical User Interface,图形用户界面)开发是一种关系到
用户和计算机交互的技术，直接影响到终端用户的使用感受以及GUI软件的使用效率。

常见GUI开发库
tkinter,python内置模块，只需导入进来即可
PyGTK C语言开发的跨平台的图形界面开发库，需要安装开发环境,这里不展示示例
http://www.pygtk.org
PyQT  与GTK图形用户界面开发库，同样有丰富的窗口部件类库，并扩展为跨平台的应用开发框架
http://www.riverbankcomputing.co.uk/software/pyqt  pip install PyQt5==5.11.3
"""
import tkinter

# root = tkinter.Tk()
# word = tkinter.Label(root, text="hello,world!")
# word.pack()
# root.mainloop()

# class App:
#     def __init__(self, master):
#         frame = tkinter.Frame(master)
#         frame.pack()
#         self.hello = tkinter.Button(frame, text="Hello", command=self.hello)
#         self.hello.pack(side=tkinter.LEFT)
#         self.quit = tkinter.Button(frame, text="Quit", fg='red', command=frame.quit)
#         self.quit.pack(side=tkinter.RIGHT)
#     def hello(self):
#         print("Hello,world!")
#
# root = tkinter.Tk()
# # 设置标题
# root.wm_title("Hello")
# # 设置窗口大小
# root.wm_minsize(200, 200)
# app = App(root)
#
# root.mainloop()
#
# # 查看Button.pack 方法中相关参数信息
# help(tkinter.Button.pack)

#######################PyQt5 实现用户图形界面的2种方式############################
"""
网上百度多是PyQt4的教程，从PyQt5开始改版比较大
"""
import sys
from PyQt5 import QtGui, QtWidgets

class CustomWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtGui.QWindow.__init__(self, parent)

        self.setFixedSize(200, 120)
        self.setWindowTitle('PyQt5 窗口')
        self.quit = QtWidgets.QPushButton('Quit', self)
        self.quit.setGeometry(62, 40, 75, 30)
        self.quit.setFont(QtGui.QFont('Times', 18, QtGui.QFont.Bold))
        self.quit.clicked.connect(self.quit_click)

    def quit_click(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
widget = CustomWidget()
widget.show()
sys.exit(app.exec_())



# def btn_clicked(self):
#     btn.setText('我被点了')
#
# app = QtWidgets.QApplication([])
# # 申明主窗体
# main_window = QtWidgets.QWidget()
# # 定义窗体大小
# main_window.resize(600, 480)
# main_window.setWindowTitle('PyQt5 窗口')
# btn = QtWidgets.QPushButton('Quit', main_window)
# btn.setGeometry(62, 40, 75, 30)
# btn.setFont(QtGui.QFont('Times', 18, QtGui.QFont.Bold))
# btn.clicked.connect(btn_clicked)
# main_window.show()
# app.exec()