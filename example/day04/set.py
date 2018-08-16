#!/usr/bin/env python3
# -*- coding=utf-8 -*-

seta = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print (seta)

seta.add('peach')
print (seta)

setb = set('abracadabra')
print (setb)

# set可以进行集合运算

a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素

setc = set(("Google", "Runoob", "Taobao"))
setc.update({1, 3})
print(setc)

# {1, 3, 'Google', 'Taobao', 'Runoob'}

setc.update([1, 4], [5, 6])
print(setc)

# {1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
