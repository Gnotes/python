# 模块

> 示例：example/day06

> Python 模块(Module)，是一个 Python 文件，以 `.py` 结尾，包含了 `Python 对象定义` 和 `Python语句`

## import 语句

想使用 Python 源文件，只需在另一个源文件里执行 `import` 语句，语法如下

```py
import module1[, module2[,... moduleN]
```

引入指定的模块

> 一个模块只会被导入一次，不管你执行了多少次import  
> 使用import语句的时候，涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块，  
> 搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在 `sys` 模块中的 `path` 变量  

```py
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages']
```

> sys.path 输出是一个列表，其中 *第一项是空串 `''`*，代表 *当前目录*

## from … import 语句

> from 语句让你从模块中 `导入` 一个 `指定的部分` 到当前命名空间中

```py
from modname import name1[, name2[, ... nameN]]
```

## from … import * 语句

> 把一个模块的 `所有内容` 全都导入到当前的命名空间

注意 ⚠️ ：这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。大多数情况不应使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义

## __name__属性

一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 `__name__` 属性来使该程序块仅在该模块自身运行时执行

> 注意 ⚠️： 每个模块都有一个 `__name__` 属性，当其值是 `__main__` 时，表明该模块自身在运行，否则是被引入

## 标准模块

> 略

## 包

包是一种管理 Python 模块 `命名空间` 的形式，采用 `点模块名称`

> 比如一个模块的名称是 `A.B` ， 那么他表示一个 `包 A` 中的 `子模块 B` 

考虑一个在 `package_example` 目录下的 `runoob1.py` 、`runoob2.py` 、`__init__.py` 文件，test.py 为测试调用包的代码，目录结构如下：

注意 ⚠️ : 目录只有包含一个叫做 `__init__.py` 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块

> 简单来说，包就是文件夹，但该文件夹下必须存在` __init__.py` 文件, 该文件的内容可以为空。`__init__.py` 用于标识当前文件夹是一个包。

> 示例：example/day06

```
test.py
package_example
|-- __init__.py
|-- runoob1.py
|-- runoob2.py
```


### 导入一个包里面的特定模块

```py
import sound.effects.echo
```

这将会导入子模块: `sound.effects.echo` 他必须 `使用全名` 去访问: 

```py
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

还有一种导入子模块的方法是  

```py
from sound.effects import echo
```

直接导入一个函数或者变量

```py
from sound.effects.echo import echofilter
```

注意 ⚠️ : 当使用 `from package import item` 这种形式的时候，对应的item既可以是 *包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量*  

> 导入语句遵循如下规则：如果包定义文件 `__init__.py` 存在一个叫做 `__all__` 的列表变量，那么在使用 `from package import *` 的时候就把这个列表中的所有名字作为包内容导入。

## __all__

> 略

## 参考

- [菜鸟 - 模块](http://www.runoob.com/python/python-modules.html)
- [菜鸟 - Python3 模块](http://www.runoob.com/python3/python3-module.html)
