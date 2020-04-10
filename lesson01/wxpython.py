#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 12:14
# @Author  : tanxw
# @Desc    : 认识 WxPython

"""
WxPython 开发库   http://wxpython.org、https://wxpython.org/pages/downloads/  安装：pip install -U wxPython
WxPython的封装： Pythoncard http://pythoncard.sourceforge.net
WxPython 开发工具(GUI设计工具)
wxGlade  http://wxglade.sourceforge.net
wxFormBuilder http://wxFormBuilder.org
Boa-constructor http://boa-constructor.sourceforge.net
"""

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
    app.MainLoop()
