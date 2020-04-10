#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 17:15
# @Author  : tanxw
# @Desc    : 文本对话框使用

import wx
# # 文本对话框
app = wx.App()
dialog = wx.TextEntryDialog(None, u'请输入文件名：', u'文件名输入', 'test.txt')
dialog.Show(True)
if dialog.ShowModal() == wx.ID_OK:
    response = dialog.GetValue()
dialog.Destroy()

app.MainLoop()