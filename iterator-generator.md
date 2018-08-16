# 迭代器与生成器

> 示例：example/day02

## 迭代器

> 迭代器是一个可以 `记住` 遍历的 `位置` 的对象，有两个基本的方法：`iter()` 和 `next()`。

```py
list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
print (next(it))   # 输出迭代器的下一个元素
print (next(it))
```

## 生成器

> 在 Python 中，使用了 `yield` 的函数被称为生成器 `generator`，这一点和 `es6` 中的概念一个意思😀。

> 跟普通函数不同的是，`生成器` 是一个 `返回迭代器` 的 `函数` ，只能用于迭代操作，个人理解为：`生成器函数，执行后返回的结果，就是一个迭代器`。

在调用生成器运行的过程中，每次遇到 `yield` 时函数会`暂停` 并 保存当前所有的运行信息，返回 `yield` 的 `值`, 并在下一次执行 `next()` 方法时从当前位置继续运行。

> 调用一个生成器函数，返回的是一个迭代器对象

```py
import sys

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
```

## 参考

- [菜鸟 - 迭代器与生成器](http://www.runoob.com/python3/python3-iterator-generator.html)