#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 16:21
# @Author  : tanxw
# @Desc    : wxPython 第一图形界面应用

import wx
import time

class CustomFrame(wx.Frame):

    def __init__(self, parent):
        # 设置窗体
        wx.Frame.__init__(self, parent, -1, 'Hello, World',
                          size=(300, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        # 创建文本窗口部件
        txt = wx.StaticText(panel, -1, 'Hello world!')
        sizer.Add(txt, 0, wx.TOP | wx.LEFT, 100)

        self.Centre()


# 自定义应用程序对象
class CustomApp(wx.App):

    def OnInit(self):
        self.frame = CustomFrame(None)
        id = self.frame.GetId()
        print("FrameID:%s" % id)
        self.frame.Show(True)
        return True

    def OnExit(self):
        print("CustomApp OnExit")
        time.sleep(2)


if __name__ == '__main__':
    print("Main start")
    # 使用从wx.App 继承的子类
    app = CustomApp()
    print("Before MainLoop")
    # 进入事件循环
    app.MainLoop()
    print("After MainLoop")