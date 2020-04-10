#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 17:37
# @Author  : tanxw
# @Desc    : 状态栏使用

import wx
class CustomFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u'简单工具栏和状态栏', size=(300, 300))

        toolbar = self.CreateToolBar()
        self.CreateStatusBar()
        self.SetStatusText(u'状态栏信息')
        toolbar.AddTool(wx.ID_EXIT, '', wx.Bitmap('./exit.png'))
        toolbar.SetSize(50, 50)

        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)
        self.Centre()

    def OnExit(self, event):
        self.Close()

app = wx.App()
frame = CustomFrame(None)
frame.Show(True)
app.MainLoop()