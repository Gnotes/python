# 字典

> 字典是可变容器，且可存储任意类型对象。  
> 以 `键值对` `key:value` 表示，多个键值对使用逗号 `,` 分隔，整个字典包括在花括号 `{}` 中

```py
dic = { key1 : value1, key2 : value2 }
```

> 值可以取任何数据类型，但`键`必须是不可变的，因此可以为 `字符串`，`数字` 或 `元组`，但是不能使用列表（列表是可变的），这一点和其他语言有些不一样哈。

```py
dict = { 'abc': 123, 98.6: 37 }
```

## 取值与复制

> 和其他语言一致，通过 `key` 访问

## 删除元素

- 使用 `del` 删除

```py
del dict['Name']; # 删除键是'Name'的元素
del dict ;        # 删除词典对象，字典将不存在
```

- clear 清空

```py
dict.clear();     # 清空词典所有元素，但是字典还存在
```

## 函数

| 函数 | 描述 |
| - | - |
| cmp(dict1, dict2) |比较两个字典元素。 |
| len(dict) |计算字典元素个数，即键的总数。 |
| str(dict) |输出字典可打印的字符串表示。 |
| type(variable) |返回输入的变量类型，如果变量是字典就返回字典类型。 |

## 方法

| 函数 | 描述 |
| - | - |
| dict.clear() | 删除字典内所有元素 |
| dict.copy() | 返回一个字典的浅复制 |
| dict.fromkeys(seq[, val]) | 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值 |
| dict.get(key, default=None) | 返回指定键的值，如果值不在字典中返回default值 |
| dict.has_key(key) | 如果键在字典dict里返回true，否则返回false |
| dict.items() | 以列表返回可遍历的(键, 值) 元组数组 |
| dict.keys() | 以列表返回一个字典所有的键 |
| dict.setdefault(key, default=None) | 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| dict.update(dict2) | 把字典dict2的键/值对更新到dict里 |
| dict.values() | 以列表返回字典中的所有值 |
| pop(key[,default]) | 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| popitem() | 随机返回并删除字典中的一对键和值。 |

## 参考

- [菜鸟 - 字典](http://www.runoob.com/python/python-dictionary.html)