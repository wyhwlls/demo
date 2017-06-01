# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#创建项目对象
app = Flask(__name__)

#加载配置文件内容
app.config.from_object('demo.setting')     #模块下的setting文件名，不用加py后缀
#app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径

#创建数据库对象

