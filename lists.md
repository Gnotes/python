# 列表

> 示例：example/day04

**列表的数据项不需要具有相同的类型**

```py
list1 = ['physics', 'chemistry', 1997, 2000]
```

## 访问列表中的值

> 列表: 个人理解为数组，根据下标访问

```py
#!/usr/bin/python
# -*- coding=utf-8 -*-


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 输出结果

list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
```

## 添加元素

```py
list = []               # 空列表
list.append('Google')   # 使用 append() 添加元素
list.append('Runoob')
```

## 删除元素

```py
list1 = ['physics', 'chemistry', 1997, 2000]
 
print(list1)
del list1[2]            # 删除下标为2的元素
print(list1)

list1.remove('physics') # 删除指定元素
print(list1)
```

## 列表脚本操作符

| Python 表达式 | 结果 | 描述 |
| - | - | - | - | 
| len([1, 2, 3]) | 3 | 长度 |
| [1, 2, 3] + [4, 5, 6] | [1, 2, 3, 4, 5, 6] | 合并列表 |
| ['Hi!'] * 4  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复 |
| 3 in [1, 2, 3] | True | 元素是否存在于列表中 |
| for x in [1, 2, 3]: print x, | 1 2 3 | 循环 |

## 列表截取

```py
L = ['Google', 'Runoob', 'Taobao']
print(L[2])  # 'Taobao' 读取列下标为2元素
print(L[-2])  # 'Runoob' 读取下标为-2的元素，倒数第二个
print(L[1:])  # ['Runoob', 'Taobao'] 读取下标为1开始至最后一个元素
```

## 列表函数&方法

- 函数

| 函数 | 描述 |
| - | - |
| cmp(list1, list2) | 比较两个列表的元素 |
| len(list) | 列表元素个数 |
| max(list) | 返回列表元素最大值 |
| min(list) | 返回列表元素最小值 |
| list(seq) | 将元组转换为列表 |

- 方法

| 函数 | 描述 |
| - | - |
| list.append(obj) | 在列表末尾添加新的对象 |
| list.count(obj) | 统计某个元素在列表中出现的次数 |
| list.extend(seq) | 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
| list.index(obj) | 从列表中找出某个值第一个匹配项的索引位置 |
| list.insert(index, obj) | 将对象插入列表 |
| list.pop([index=-1]) | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
| list.remove(obj) | 移除列表中某个值的第一个匹配项 |
| list.reverse() | 反向列表中元素 |
| list.sort(cmp=None, key=None, reverse=False) | 对原列表进行排序 |