#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import sys

list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成，只有在迭代的时候才会执行生成器里边的语句

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
