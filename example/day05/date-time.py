#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import time
import calendar

tick = time.time()
print("当前时间戳为", tick)

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print ("本年为 :", localtime.tm_year)
print ("今天为 :", localtime[0:3])

cal = calendar.month(2018, 8)
print ("以下输出2018年8月份的日历:")
print (cal)
