#!/usr/bin/env python3
# -*- coding=utf-8 -*-

while True:
    try:
        x = int(input("请输入一个数字(为了看到异常请输入非数字): "))
        break
    except ValueError:
        print("Oops!  😰 出错了吧，再来一次 ")

print("----------------")

if True:
    try:
        raise NameError('使用raise抛出了一个异常,并指定异常类型')
    except NameError:
        print('捕获到异常，但是不处理，使用raise 直接向外抛出!')
        raise
