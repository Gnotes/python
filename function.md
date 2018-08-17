# 函数

> 示例：example/day05

## 函数定义

```
def 函数名（参数列表）:
    函数体
```

如：

```py
# 计算面积函数
def area(width, height):
    return width * height


print('面积：', area(10, 20))
```

> 注意：函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明，个人理解为 `注释文字`，执行函数时，不会被解析

> `return [表达式]` 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 `None`。

## 函数参数

- `必需参数` : 即函数内调用了的参数，使用时必须传递
- `关键字参数` : 即指定参数名
- `默认参数` : 即指定参数默认值
- `不定长参数` : 多个参数时，不明确指定参数，使用 `*` 关键字指定

### 关键字参数

```py
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
#调用printme函数
printme( str="Python教程" )
```

### 默认参数

```py
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print ("名字: ", name)
    print ("年龄: ", age)
    return


# 调用printinfo函数
printinfo(name="runoob")
```

### 不定长参数

> 不定长参数使用 `*` 关键符号指定，表示多个参数，基本语法如下：

```py
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

示例：

```py
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )

# 输出结果

输出:
70
(60, 50)
```

> 如果在函数调用时 `没有指定参数`，它就是一个 `空元组`。我们也 `可以不传递` `命名的变量` (不定长参数)。如

```py
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 ) # 未传递不定长参数
printinfo( 70, 60, 50 )
```

> 注意：还有一种就是参数带两个星号 `**`，参数以 `字典` 的形式 `导入` ，基本语法如下

```py
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

示例：

```py
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
   print (vardict['a'])
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)

# 输出结果

输出:
1
{'a': 2, 'b': 3} # 这个是字典
2
```

> 声明函数时，参数中星号 `*` 可以单独出现，例如

```py
def f(a,b,*,c):
    return a+b+c

f(1,2,3)   # 报错
f(1,2,c=3) # 正常
```

## 匿名函数

python 使用 `lambda` 来创建匿名函数，即不再使用 `def` 语句的形式定义一个函数，基本语法如下：

```
lambda [arg1 [,arg2,.....argn]]:expression
```

```py
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
```

## 变量作用域

> Python 中，作用域决定于这个 `变量是在哪里赋值的`，Python的作用域一共有4种

- `L` :（Local） 局部作用域
- `E` :（Enclosing） 闭包函数外的函数中
- `G` :（Global） 全局作用域
- `B` :（Built-in） 内建作用域

> 以 `L –> E –> G –>B` 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找

```py
x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
```

> Python 中只有 `模块`（module），`类`（class）以及 `函数`（def、lambda）才 `会引入新的作用域`，即有作用域限制  
> 其它的代码块（如 `if/elif/else/`、`try/except`、`for/while` 等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，即相对于没有作用域限制

```py
>>> if True:
...  msg = 'I am from Runoob'
... 
>>> msg # 可以访问到if代码块中定义的msg
'I am from Runoob'
```

> 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问

## 全局变量和局部变量

> 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域

```py
total = 0 # 这是一个全局变量

def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)
```

## global 和 nonlocal关键字

> 当内部作用域想修改 `外部作用域` 的 `变量` 时，就要用到 `global` 和 `nonlocal` 关键字了

```py
#!/usr/bin/python3
 
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)
```

> 如果要修改 `嵌套作用域`（enclosing 作用域，外层非全局作用域）中的 `变量` 则需要 `nonlocal` 关键字了

```py
#!/usr/bin/python3
 
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
```

## 参考

- [菜鸟 - 函数](http://www.runoob.com/python3/python3-function.html)