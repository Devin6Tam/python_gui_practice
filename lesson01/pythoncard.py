#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 16:33
# @Author  : tanxw
"""
PythonCard 依然维持2006年的版本，所以只能用于python2版本
"""
from PythonCard import model

class Minimal(model.Background):
    pass

if __name__ == '__main__':
    app = model.Application(Minimal)
    app.MainLoop()