#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask

#创建flask应用
app = Flask(__name__)

#读取应用配置文件(config.py)
app.config.from_object('config')

#加载视图
from app import views
