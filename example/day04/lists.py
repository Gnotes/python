#!/usr/bin/python
# -*- coding=utf-8 -*-


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

print(list1)
del list1[2]
print(list1)

list1.remove('physics')
print(list1)


L = ['Google', 'Runoob', 'Taobao']
print(L[2])  # 'Taobao'
print(L[-2])  # 'Runoob'
print(L[1:])  # ['Runoob', 'Taobao']
