#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# 计算面积函数


def area(width, height):
    return width * height


print('面积：', area(10, 20))


def printme(str):
    "打印任何传入的字符串"  # 第一行函数说明文字
    print (str)
    return


# 调用printme函数
printme(str="Python教程")


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print ("名字: ", name)
    print ("年龄: ", age)
    return


# 调用printinfo函数
printinfo(name="runoob")


def printinfo1(arg1, *vartuple):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    print (vartuple)


# 调用printinfo 函数
printinfo1(70, 60, 50)


def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return


# 调用printinfo 函数
printinfo2(10)  # 未传递不定长参数
printinfo2(70, 60, 50)


def printinfo3(arg1, **vardict):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    print (vardict)
    print (vardict['a'])


# 调用printinfo 函数
printinfo3(1, a=2, b=3)


# def funs(a, b, *, c):
#     return a+b+c


def funs(a, b, *, c):
    return a + b + c


# funs(1, 2, 3)         # 报错
print(funs(1, 2, c=3))  # 正常
