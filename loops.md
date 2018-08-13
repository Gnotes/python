# 循环

> 示例： example/day02

> Python提供了for循环和while循环 `（在Python中没有do..while循环）`

注：`嵌套循环` 你可以在while循环体中嵌套for循环

## 循环控制语句

| 运算符 | 描述 |
| - | - | - |
| break 语句 | 在语句块执行过程中终止循环，并且跳出整个循环 |
| continue 语句 | 在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。 |
| pass 语句 | pass是空语句，是为了保持程序结构的完整性。 |

## while

基本语法

```py
while 判断条件：
    执行语句……
```

#### 循环使用 else 语句

> 在 python 中，`while … else` 在循环条件为 false 时执行 else 语句块：

```py
#!/usr/bin/python
 
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

# 输出结果

0 is less than 5
1 is less than 5
2 is less than 5
3 is less than 5
4 is less than 5
5 is not less than 5
```

## for 循环语句

基本语法

```py
for iterating_var in sequence:
   statements(s)
```

示例：

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for l in 'Python':     # 第一个实例
    print('当前字母 :', l)

fruits = ['banana', 'apple', 'mango']
for f in fruits:        # 第二个实例
    print('当前字母 :', f)
```

#### 通过序列索引迭代

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

fruits = ['banana', 'apple', 'mango'] 
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])
```

> 以上实例我们使用了内置函数 `len()` 和 `range()`,函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数

#### 循环使用 else 语句

> 在 python 中，`for … else` 表示这样的意思，for 中的语句和普通的没有区别，`else` 中的语句会在循环 `正常` 执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，`while … else` 也是一样。

```py

for num in range(10, 20):    # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:     # 确定第一个因子
            j = num/i        # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break            # 跳出当前循环
    else:                    # 循环的 else 部分
        print(num, '是一个质数')
```

## 循环嵌套

- for 循环嵌套语法:

```py
for iterating_var in sequence:
    for iterating_var in sequence:
        statements(s)
    statements(s)
```

- while 循环嵌套语法:

```py
while expression:
    while expression:
        statement(s)
    statement(s)
```

## break 语句

> `break` 语句，就像在C语言中，打破了最小封闭for或while循环。

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':     # 第一个实例
    if letter == 'h':
        break
    print('当前字母 :', letter)

print('------------------')

var = 10                    # 第二个实例
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:   # 当变量 var 等于 5 时退出循环
        break
```

## continue 语句

> `continue` 语句跳出本次循环，而` break` 跳出整个循环

> 略

## pass 语句

> `pass` 是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句。

```py
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
```

## 参考

- [菜鸟 - 循环](http://www.runoob.com/python/python-loops.html)