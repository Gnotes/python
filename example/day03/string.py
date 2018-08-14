#!/usr/bin/env python3
# -*- coding=utf-8 -*-

var1 = 'Hello World!'
var2 = "Python"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print('------------------')

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

print('str.format函数格式化：')
print("{} {}".format("hello", "world"))        # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world"))      # 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置


print("网站名：{name}, 地址 {url}".format(
    name="xinghe", url="github.com/Gnotes/Python"))
# 通过字典设置参数
site = {"name": "xinghe", "url": "github.com/Gnotes/Python"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['xinghe', 'github.com/Gnotes/Python']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


class AssignValue(object):
    def __init__(self, value):
        self.value = value


my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
print('value 为: {.value}'.format(my_value))   # 没有"0"
