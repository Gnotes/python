# 运算符

Python语言支持以下类型的运算符:

- 算术运算符
- 比较（关系）运算符
- 赋值运算符
- 逻辑运算符
- 位运算符
- 成员运算符
- 身份运算符
- 运算符优先级

## Python算术运算符

以下假设变量： a=10，b=20：

| 运算符 | 描述 | 实例 | 
| - | - | - |
| + | 加 - 两个对象相加 | a + b 输出结果 30 |
| - | 减 - 得到负数或是一个数减去另一个数 | a - b 输出结果 -10 |
| * | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 200 |
| / | 除 - x除以y | b / a 输出结果 2 |
| % | 取模 - 返回除法的余数 | b % a 输出结果 0 |
| **  | 幂 - 返回x的y次幂 | a**b 为10的20次方， 输出结果 100000000000000000000 |
| //  | 取整除 - 返回商的整数部分（向下取整） | 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0 |

> 注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可

```py
>>> 1/2
0
>>> 1.0/2
0.5
>>> 1/float(2)
0.5
```

## Python比较运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述 | 实例 | 
| - | - | - |
| ==  | 等于 - 比较对象是否相等 | (a == b) 返回 False。 |
| !=  | 不等于 - 比较两个对象是否不相等 | (a != b) 返回 true. |
| <>  | 不等于 - 比较两个对象是否不相等 | (a <> b) 返回 true。这个运算符类似 != 。 |
| > | 大于 - 返回x是否大于y | (a > b) 返回 False。 |
| < | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。 | (a < b) 返回 true。 |
| >= | 大于等于  - 返回x是否大于等于y。|  (a >= b) 返回 False。 |
| <= | 小于等于 -  返回x是否小于等于y。|  (a <= b) 返回 true。 |

## Python赋值运算符

以下假设变量a为10，变量b为20：

| 运算符 | 描述 | 实例 | 
| - | - | - |
| = | 简单的赋值运算符 |  c = a + b 将 a + b 的运算结果赋值为 c |
| +=  | 加法赋值运算符 | c += a 等效于 c = c + a |
| -=  | 减法赋值运算符 | c -= a 等效于 c = c - a |
| *=  | 乘法赋值运算符 | c *= a 等效于 c = c * a |
| /=  | 除法赋值运算符 | c /= a 等效于 c = c / a |
| %=  | 取模赋值运算符 | c %= a 等效于 c = c % a |
| **= | 幂赋值运算符 |  c **= a 等效于 c = c ** a |
| //= | 取整除赋值运算符 |  c //= a 等效于 c = c // a |

## Python位运算符

> 略

## Python逻辑运算符

以下假设变量 a 为 10, b为 20:

| 运算符 | 描述 | 实例 | 
| - | - | - |
| and | x and y 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。| (a and b) 返回 20。 |
| or | x or y  布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。| (a or b) 返回 10。 |
| not | not x 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

## Python成员运算符

> 个人理解为判断是否属于某个对象的操作

| 运算符 | 描述 | 实例 | 
| - | - | - |
|in | 如果在指定的序列中找到值返回 True，否则返回 False。| x 在 y 序列中 , 如果 x 在 y 序列中返回 True。 |
|not in  | 如果在指定的序列中没有找到值返回 True，否则返回 False。| x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

## Python身份运算符

> 身份运算符用于比较两个对象的存储单元，个人理解为是否两个对象相等，即引用内存地址是否相同

  **注：** `id()` 函数用于获取对象内存地址

| 运算符 | 描述 | 实例 | 
| - | - | - |
| is | is 是判断两个标识符是不是引用自一个对象 | x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

## Python运算符优先级

> 略

## 参考

- [菜鸟 - 运算符](http://www.runoob.com/python/python-operators.html)