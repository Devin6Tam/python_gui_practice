#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 17:34
# @Author  : tanxw
# @Desc    : 消息对话框使用

import wx

# # 消息对话框
app = wx.App()
dialog = wx.MessageDialog(None, u'确认删除吗？', u'文件删除',
                          wx.YES_NO | wx.ICON_QUESTION)
dialog.Show(True)
result = dialog.ShowModal()
print(result)
dialog.Destroy()
app.MainLoop()