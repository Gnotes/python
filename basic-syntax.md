# 基础语法

> 示例：`example/day01`

## 指定解析器

Python文件后缀为`.py`，在 `py` 文件头部指定该文件执行时的解析器，如：

```py
#!/usr/bin/python
```

## 编码格式

Python 中常用的编码格式方法有如下两种：

1. 带等于号的：  

```py
# coding=<encoding name>
```

2. 最常见的，带冒号的（大多数编辑器都可以正确识别的）：  

```py
# -*- coding: <encoding name> -*-
```

## Python 标识符

- 在 Python 里，标识符由`字母` 、`数字` 、`下划线组成`。
- 在 Python 中，所有标识符可以包括`英文`、`数字`以及`下划线(_)`，但 `不能以数字开头`。
- Python 中的标识符是`区分大小写`的。
- 以下划线开头的标识符是有特殊意义的。以`单下划线开头` `_foo` 的代表 `不能直接访问的类属性`，需通过类提供的 `接口进行访问`，不能用 `from xxx import *` 而导入；
- 以`双下划线开头` 的 `__foo` 代表 `类` 的`私有成员`；以`双下划线` `开头`和 `结尾`的 `__foo__` 代表 Python 里`特殊方法专用的标识` ，如 `__init__()` 代表类的`构造函数`。
- Python 可以同一行显示多条语句，方法是用分号 `;` 分开，如：

```py
>>> print('hello'); print('Python');
hello
Python
```

## Python 保留字符

> 下面的列表显示了在Python中的保留字。这些保留字不能用作 `常量` 或 `变量`，或任何其他 `标识符名称`。

| | | | | |
|-|-|-|-|-|
| and | exec | not | assert | finally |
| or | break | for | pass | class |
| from | print | continue | global | yield |
|raise | def | if | return | del |
| import | try | elif | in | while | 
| else | is | with | except | lambda |

## 行和缩进

Python 与其他语言最大的区别就是，`Python 的代码块不使用大括号 {} ` 来控制类，函数以及其他逻辑判断。python 最具特色的就是用 `缩进` 来写模块

> 缩进的空白数量是可变的，但是`所有代码块语句` 必须包含 **`相同`** 的 `缩进空白数量`，这个 **`必须严格执行`** 。如下所示

> 如下代码中 `if` 后边是一个代码块，`else` 里边的是一个代码块，因此同一个代码块中缩进一致就不会提示错误，但是最好所有缩进保持一致.如：

```py
if True:
  print("Answer")
  print("True")
else:
    print("Answer")
    print("False")
```

但是，同一个代码块中缩进不一致，将会报错.

```py
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    # 没有严格缩进，在执行时会报错
  print("False")
```

```py
  File "intent.py", line 10
    print("False")
                 ^
IndentationError: unindent does not match any outer indentation level
```

- `IndentationError: unindent does not match any outer indentation level`  
  > 错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。

- `IndentationError: unexpected indent`  
  > 则 python 编译器是在告诉你"文件里格式不对了，可能是tab和空格没对齐的问题"

## 多行语句

> Python语句中一般以 `新行` 作为语句的 `结束符` 。但是我们可以使用`斜杠（ \）`将一行的语句分为多行显示，如下所示：

```py
total = item_one + \
        item_two + \
        item_three
```

但语句中包含 `[]`, `{}` 或 `()` 括号就不需要使用多行连接符。如下实例

```py
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

## Python 引号

Python 可以使用引号( `'` )、双引号( `"` )、三引号( `'''` 或 `"""` ) 来表示`字符串`，引号的开始与结束必须的相同类型的。

其中`三引号` **可** 以由`多行`组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

```py
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
```

## Python 注释

python中单行注释采用 `#` 开头。

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 第一个注释
print "Hello, Python!";  # 第二个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
```

## Python 空行

> 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

> 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

**记住：空行也是程序代码的一部分**

## 等待用户输入

下面的程序执行后就会等待用户输入，按回车键后就会退出：

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

raw_input("按下 enter 键退出，其他任意键显示...\n")
```

以上代码中 ，`\n` 实现换行。一旦用户按下 enter(回车) 键退出

## 同一行显示多条语句

Python可以在同一行中使用多条语句，语句之间使用 `分号(;)` 分割，以下是一个简单的实例：

```py
#!/usr/bin/python

import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

## Print 输出

> print 默认输出是换行的，如果要实现 `不换行` 需要在 `变量末尾` 加上`逗号 ,`

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
```

## 多个语句构成代码组

> 缩进相同的一组语句构成一个代码块，我们称之代码组。

> 像 `if` 、`while`、`def` 和 `class` 这样的复合语句，首行以关键字开始，以冒号( `:` )结束，该行之后的一行或多行代码构成代码组。

> 我们将首行及后面的代码组称为一个 `子句`(clause)。

如下实例：

```py
if expression : 
   suite 
elif expression :  
   suite  
else :  
   suite 
```

## Python解释器

> Python 执行的解析器

- [Python解释器](http://www.runoob.com/python3/python3-interpreter.html)


## end 关键字

关键字 `end` 可以用于将结果 `输出到同一行`，或者在 输出的 `末尾` 添加不同的 `字符` ，实例如下

```py
#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

# 输出结果

1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```
