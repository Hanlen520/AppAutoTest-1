#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> PublicFunc
# @Author ：Zhang Jing
# @Date   ：2020/5/14 20:28
# @Desc   ：
import json
import os
# 处理邮件内容的库
import shutil
import smtplib
from email.mime.text import MIMEText
# 发送邮件附件 需要导入别的库  MIMEMultipart,Header,MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase

import jinja2
from airtest.core.api import *
from airtest.report.report import simple_reports

from Base.BaseSettings import LOG_DIR, DEVICES, TEST_REPORT_HTML, TEST_REPORT_RESULTDATA


def send_email(email_Subject, file_path, filename, received_Email=["邮箱列表"], mailserver="smtp.qq.com",
               userName_SendEmail='邮箱', userName_AuthCode='邮箱码'):
    mailserver = mailserver
    userName_SendEmail = userName_SendEmail
    userName_AuthCode = userName_AuthCode
    received_Email = received_Email

    print(file_path)
    # 创建邮件对象
    msg = MIMEMultipart()

    msg["Subject"] = Header(email_Subject, 'utf-8')
    msg["From"] = userName_SendEmail
    msg["To"] = ",".join(received_Email)

    content = open(file_path, 'rb').read()
    # # 发送普通文本
    html_content = MIMEText(content, 'html', 'utf-8')
    msg.attach(html_content)

    # 邮件中发送附件
    att = MIMEText(content, "base64", "utf-8")

    att["Content-Type"] = "application/octet-stream"  # 一种传输形式
    att["Content-Disposition"] = "attachment;filename=%s" % filename
    msg.attach(att)

    smtp = smtplib.SMTP_SSL(mailserver)  # 创建客户端
    smtp.login(userName_SendEmail, userName_AuthCode)
    smtp.sendmail(userName_SendEmail, ",".join(received_Email), msg.as_string())
    smtp.quit()


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new, lists[-1]


def make_dir(filename, funcname):
    """
        用于生成日志
    @param filename:  文件名
    @param funcname:  函数名
    @return:
    """
    Log_dir = os.path.join(LOG_DIR, filename)
    logdir = os.path.join(Log_dir, funcname)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    else:
        shutil.rmtree(logdir)
        os.makedirs(logdir)
    return logdir


def output_report(file, logpath, output, testname, testtitle, testdesc=None):
    """
    @param file:   __file__
    @param logpath: ,logdir  日志路劲
    @param output:  "testpremeetingcount.html"  输出文件名
    @param testname: ,"zj"
    @param testtitle: ,"测试班前会统计"
    @param testdesc: "用来测试班前会统计"
    """
    html_output = os.path.join(TEST_REPORT_HTML, output)
    data = simple_reports(file, testname, testtitle, testdesc, logpath=logpath, output=html_output)

    txt_output = output.replace(".html", ".txt")
    txt_output = os.path.join(TEST_REPORT_RESULTDATA, txt_output)
    with open(txt_output, "w", encoding="utf-8") as f:
        f.write(data)


def appinitialize(file, logdir, devices=DEVICES):
    auto_setup(file, logdir=logdir, devices=devices)
    stop_app("com.runyunba.asbm")
    sleep(2)
    start_app("com.runyunba.asbm")

def Iosappinitialize(file, logdir, devices=DEVICES):
    auto_setup(file, logdir=logdir, devices=devices)
    stop_app("com.rby.SafeManager")
    sleep(2)
    start_app("com.rby.SafeManager")

def output_converge_report(result_report_name="report_result.html"):
    results = []
    dirs = os.listdir(TEST_REPORT_HTML)
    for html in dirs:
        if html.endswith(".html"):
            result_txt = html.replace('.html', '.txt')
            result_txt = os.path.join(TEST_REPORT_RESULTDATA, result_txt)
            result_dict = json.load(open(result_txt, 'r'))
            result_dict['html_path'] = os.path.join(TEST_REPORT_HTML, html)
            result_dict['html_name'] = html.replace('.html', '')
            result_dict['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(round(result_dict["run_start"])))
            result_dict["time"] = round(result_dict["run_end"] - result_dict["run_start"], 1)

            results.append(result_dict)

    root_dir = "D:\\Pycharm\\PythonProject\\APPAutoTest"
    # 生成聚合报告
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(root_dir),
        extensions=(),
        autoescape=True
    )
    template = env.get_template("converge_template.html", root_dir)
    html = template.render({"results": results})
    output_file = os.path.join(root_dir, result_report_name)
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(html)

    send_email("测试报告", output_file, result_report_name)  # 调用发送邮件模块

if __name__ == '__main__':
    pass
