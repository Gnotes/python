# 输入与输出

> 示例：example/day07

## 读取键盘输入

Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘

- `raw_input` : 从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
- `input` : 可以接收一个Python表达式作为输入，并将运算结果返回

> 注意 ⚠️ `python3` 将 `raw_input` 和 `input` 进行了整合，**只有 `input`**

```py
# str = raw_input("请输入：")
str = input("请输入：")
print("str: ", str)
```

## 读写文件

> 略

详细内容查看参考文档

## 参考

- [菜鸟 - I/O](http://www.runoob.com/python/python-files-io.html)
- [菜鸟 - Python3 I/O](http://www.runoob.com/python3/python3-inputoutput.html)