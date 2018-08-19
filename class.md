# 类

> 示例：example/day07

## 类定义

```py
class ClassName(SuperClass,...) :
    ...
```

- `__init__()` 的特殊方法（构造方法）
- `self` 参数，`类方法` 与普通的函数只有一个 `区别`，类方法 `必须` 有一个额外的 `第一个参数` 名称即 `self`，`self` 不是关键字可以自定义
- 子类可以覆写父类方法，与其他语言一样。继承多个父类是，如果有多个同名方法，则 *根据继承顺序，**取先继承的类** 中方法* ，如下多继承中的 `Sample.speak` ，就使用的是第一个继承的类 `Speaker` 中的方法.

```py
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = People('runoob', 10, 30)
p.speak()
```

> 类实例化直接 `Class(*args)`  
> 属性引用使用 `instance.name` 的方式  

## 类继承

- 单继承

```py
# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = Student('ken', 10, 60, 3)
s.speak()
```

- 多继承

```py
class Speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
```

### 属性检测

- `getattr(instance, name[, default])` : 访问对象的属性。
- `hasattr(instance,name)` : 检查是否存在一个属性。
- `setattr(instance,name,value)` : 设置一个属性。如果属性不存在，会创建一个新属性。
- `delattr(instance, name)` : 删除属性。

### 内置 `类` 属性

- `__dict__` : 类的属性（包含一个字典，由类的数据属性组成）
- `__doc__` :类的文档字符串
- `__name__`: 类名
- `__module__`: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
- `__bases__` : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

## 类检测

- `issubclass()` 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
- `isinstance(obj, Class)` 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

## 类属性与方法

- 类的私有属性

> `__private_attrs`：`两个下划线开头`，声明该属性为`私有属性`，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

- 类的方法

> 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

- 类的私有方法

> `__private_method`：`两个下划线开头`，声明该方法为`私有方法`，不能在类的外部调用。在类的内部调用 self.__private_methods

## 单下划线、双下划线、头尾双下划线说明：

- `首尾双下划线` 如 `__init__()` : 定义的是特殊方法，一般是 `系统定义`
- `单下划线开头` 如 `_foo` : 表示的是 `protected` 类型的变量，即保护类型只能允许其本身与子类进行访问，`不能用于 from module import *`
- `双下划线开头` 如 `__foo` : 表示的是 `私有类型(private)` 的变量, 只能是允许这个类本身进行访问了

## 子类继承父类构造函数说明

- `__init__` 为构造
- `子类` **不重写** `__init__`，实例化子类时，会 `自动调用` **父类** 定义的 `__init__`
- 如果重写了 `__init__` 时，实例化子类，就 `不会自动调用` 父类已经定义的 `__init__`
- 继承父类的构造方法，可以使用 `super` 关键字

```py
super(子类，self).__init__(参数1，参数2，....)
# 或者
父类名称.__init__(self,参数1，参数2，...)
```

## 参考

- [菜鸟 - Python3 类](http://www.runoob.com/python3/python3-class.html)
- [菜鸟 - 类](http://www.runoob.com/python/python-object.html)
- [菜鸟 - Python3 子类继承父类构造说明](http://www.runoob.com/w3cnote/python-extends-init.html)