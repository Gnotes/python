#!/usr/bin/env python3
# -*- coding=utf-8 -*-

counter = 100   # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"   # 字符串

print(counter, miles)

a = b = c = 1

print(a, b, c)

a, b, c, d = counter, miles, name, True

print(a, b, c, d)


student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素
