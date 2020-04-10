#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 17:00
# @Author  : tanxw

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

        self.button = wx.Button(panel, -1, "Hello world!")
        sizer.Add(self.button, 0, wx.TOP | wx.LEFT, 100)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindow)
        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)

        self.Centre()

    def OnClick(self):
        self.Close(True)

    def OnEnterWindow(self, event):
        self.button.SetLabel(u"退出（鼠标进入）")
        event.Skip()

    def OnLeaveWindow(self, event):
        self.button.SetLabel(u"退出（鼠标离开）")
        event.Skip()

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
    # 使用从wx.App 继承的子类
    app = CustomApp()
    # 进入事件循环
    app.MainLoop()