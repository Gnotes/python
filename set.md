# 集合

> 示例：example/day04

> 集合（set）是一个无序不重复元素的序列，可以使用大括号 `{ }` 或者 `set()` 函数创建集合

> 注意 ⚠️ ：创建一个空集合必须用 `set()` 而不是 `{ }`，因为 `{ }` 是用来创建一个 `空字典`

```py
# set可以进行集合运算

a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素
```

## 添加元素

```py
s.add( x )
```

*还有一个方法，也可以添加元素，且 参数 可以是 `列表`，`元组`，`字典` 等，语法格式如下*

```py
s.update( x )
```

```py
setc = set(("Google", "Runoob", "Taobao"))
setc.update({1, 3})
print(setc)

# {1, 3, 'Google', 'Taobao', 'Runoob'}

setc.update([1, 4], [5, 6])
print(setc)

# {1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
```

> 以上示例可以看出传入的参数将会转化为 `set` 单个元素，进行处理

## 移除元素

```py
s.remove( x )
```

> 还有一个方法也是移除集合中的元素，且如果 `元素不存在，不会发生错误`。

```py
s.discard( x )
```

> `随机` 删除集合中的 `一个` 元素

```py
s.pop() 
```

## 元素个数

```py
len(s)
```

## 清空集合

```py
s.clear()
```

## 否在存在集合中

```py
x in s
```

## 参考

- [菜鸟 - 集合](http://www.runoob.com/python3/python3-set.html)