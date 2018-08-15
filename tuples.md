# 元组

> Python的元组与列表类似，不同之处在于 `元组的元素不能修改`。  
> 元组使用 `小括号 ()`，列表使用方括号。  
> 元组创建很简单，只需要在括号中添加元素，并使用 `逗号` 隔开即可

```py
#!/usr/bin/python

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
```

> 注意： 任意无符号的对象，以逗号隔开，默认为元组，如上的 `tup3`

## 修改元组

> 注意：元组是不能被修改的，但是可以对元组进行 `连接(合并)` 操作

```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)
```

# 删除元组

元组的删除和列表一致，使用 `del`

```py
tup = ('physics', 'chemistry', 1997, 2000)
 
print(tup)
del tup
print("After deleting tup : ")
print(tup) # 报错
```

> 元组被删除后，输出变量会有异常信息

```py
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print tup
NameError: name 'tup' is not defined
```

## 运算符

> 略

和列表一致，包含

- `len`
- `+`
- `*`
- `in`
- `for x in xxx`

## 元组索引，截取

> 略

和列表一致，通过下标 `[]` `[:]`

## 内置函数

| 函数 | 描述 |
| - | - |
| cmp(tuple1, tuple2) | 比较两个元组元素。 |
| len(tuple) | 计算元组元素个数。 |
| max(tuple) | 返回元组中元素最大值。 |
| min(tuple) | 返回元组中元素最小值。 |
| tuple(seq) | 将列表转换为元组。 |
