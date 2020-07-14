#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> BasePage
# @Author ：ZhangJing
# @Date   ：2020/5/13 16:03
# @Desc   ：基础类，用于页面对象类的继承
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
class Page(object):
    """
    基础类，用于页面对象类的继承
    """

    def __init__(self, ):
        """

        :type driver: object
        """

        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        if not cli_setup():
            auto_setup(__file__, logdir=True, devices=[
                "Android://127.0.0.1:5037/d604cbf",
            ])
        print("start...")

if __name__ == '__main__':
    page = Page()