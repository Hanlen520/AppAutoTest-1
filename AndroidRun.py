#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File   ：AutoTest -> run
# @Author ：Zhang Jing
# @Date   ：2020/5/18 9:22
# @Desc   ：

from Base.PublicFunc import output_converge_report
from AndroidTestSuite.TestSuite1 import testsuite1

testsuite1()
output_converge_report("Android_report_result.html")
