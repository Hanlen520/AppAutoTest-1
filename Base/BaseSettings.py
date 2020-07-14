#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> BaseSetting
# @Author ：Zhang Jing
# @Date   ：2020/5/13 17:34
# @Desc   ：一些基本的配置参数
import json
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "logs")

# 0不开启DEBUG对应线上模式  1开启DEBUG模式
DEBUG_MODEL = 1
# 本地chromdriver
local_chromdriver = "D:\Pycharm\PythonProject\AutoTest\driver\chromedriver.exe"

# 测试数据文件
TEST_DATA_YAML = os.path.join(BASE_DIR, "TestData")
TEST_REPORT_HTML = os.path.join(BASE_DIR, "report\\html\\")
TEST_REPORT_RESULTDATA = os.path.join(BASE_DIR, "report\\resultdata\\")
TEST_REPORT_XLSX = os.path.join(BASE_DIR, "report\\xlsx\\")

MYSQL_HOST = '127.0.0.1'  # polardb 数据库
MYSQL_DBNAME = 'test'  # 数据库名字   正式环境，请修改
MYSQL_USER = 'root'  # 数据库账号，请修改
MYSQL_PASSWD = ''  # 数据库密码，请修改
MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

DEVICES = ["Android://127.0.0.1:5037/d604cbf"]
#IOSDEVICES = ["ios:///http://192.168.0.167:8100"]
IOSDEVICES = ["ios:///http://127.0.0.1:8100"]  # gwc
# IOSDEVICES = ["Android://127.0.0.1:5037/d604cbf"]
