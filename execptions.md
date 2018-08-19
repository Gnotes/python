# 错误与异常

> 示例：example/day07

## 异常处理

基本语法：

```py
try :
  ...
except ErrName :
  ...
except ErrName :
  ...
except ErrName :
  ...
else :
  ...
finally :
  ...

# 或者是

try :
  ...
except (ErrName, ErrName, ErrName) :
  ...
else :
  ...
finally :
  ...
```

示例：

```py
#!/usr/bin/env python3
# -*- coding=utf-8 -*-

while True:
    try:
        x = int(input("请输入一个数字(为了看到异常请输入非数字): "))
        break
    except ValueError:
        print("Oops!  😰 出错了吧，再来一次 ")
```

## 抛出异常

> 使用 `raise` 语句抛出一个指定的异常

```py
if True:
    try:
        raise NameError('使用raise抛出了一个异常,并指定异常类型')
    except NameError:
        print('捕获到异常，但是不处理，使用raise 直接向外抛出!')
        raise

# 输出结果

捕获到异常，但是不处理，使用raise 直接向外抛出!
Traceback (most recent call last):
  File "example/day07/excp.py", line 15, in <module>
    raise NameError('使用raise抛出了一个异常,并指定异常类型')
NameError: 使用raise抛出了一个异常,并指定异常类型
```

## 自定义异常

> 略

稍后补充

## 参考

- [菜鸟 - 错误与异常](http://www.runoob.com/python3/python3-errors-execptions.html)