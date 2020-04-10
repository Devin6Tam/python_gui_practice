#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 16:18
# @Author  : tanxw
# @Desc    : wxPython 第一个用户图形界面

import wx

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

if __name__ == '__main__':
    app = wx.App()
    frame = CustomFrame(None)
    frame.Show(True)
    # 进入事件循环
    app.MainLoop()