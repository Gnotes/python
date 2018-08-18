# 日期和时间

> 示例：example/day05

> Python 提供了一个 `time` 和 `calendar` 模块可以用于格式化日期和时间。

注意：时间间隔是以 `秒` 为单位的 `浮点小数`。

## time 模块

```py
#!/usr/bin/python3

import time                  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks) # 输出时间戳
```

## 时间元组

> 个人理解 `时间元组` 就是使用元组的结构表示的时间对象，这个对象由 `9` 个部分组成。

| 序号 | 字段 | 描述 | 值 |
| - | - | - | - |
| 0 | tm_year | 4位数年 | 2018 |
| 1 | tm_mon | 月 | 1 到 12 |
| 2 | tm_mday | 日 | 1到31 |
| 3 | tm_hour | 小时 | 0到23 |
| 4 | tm_min | 钟 | 0到59 |
| 5 | tm_sec | 秒 | 0到61 (60或61 是闰秒) |
| 6 | tm_wday | 一周的第几日 | 0到6 (0是周一) |
| 7 | tm_yday | 一年的第几日 | 1到366 (儒略历) |
| 8 | tm_isdst | 夏令时 | -1, 0, 1, -1是决定是否为夏令时的旗帜 |

> `struct_time元组` 拥有如上的 `结构` 和 `属性`

```py
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print ("本年为 :", localtime.tm_year)
print ("今天为 :", localtime[0:3])

# 输出结果

本地时间为 : time.struct_time(tm_year=2018, tm_mon=8, tm_mday=17, tm_hour=20, tm_min=59, tm_sec=8, tm_wday=4, tm_yday=229, tm_isdst=0)
本年为 : 2018
本年为 : (2018, 8, 17)
```

## 格式化日期

> 略

- `%y` : 两位数的年份表示（00-99）
- `%Y` : 四位数的年份表示（000-9999）
- `%m` : 月份（01-12）
- `%d` : 月内中的一天（0-31）
- `%H` : 24小时制小时数（0-23）
- `%I` : 12小时制小时数（01-12）
- `%M` : 分钟数（00=59）
- `%S` : 秒（00-59）
- `%a` : 本地简化星期名称
- `%A` : 本地完整星期名称
- `%b` : 本地简化的月份名称
- `%B` : 本地完整的月份名称
- `%c` : 本地相应的日期表示和时间表示
- `%j` : 年内的一天（001-366）
- `%p` : 本地A.M.或P.M.的等价符
- `%U` : 一年中的星期数（00-53）星期天为星期的开始
- `%w` : 星期（0-6），星期天为星期的开始
- `%W` : 一年中的星期数（00-53）星期一为星期的开始
- `%x` : 本地相应的日期表示
- `%X` : 本地相应的时间表示
- `%Z` : 当前时区的名称
- `%%` : %号本身

## calendar 模块

获取某月日历

```py
import calendar

cal = calendar.month(2018, 8)
print ("以下输出2018年8月份的日历:")
print (cal)

# 输出结果

以下输出2018年8月份的日历:
    August 2018
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```

> 更多详细内容查看参考文档

在Python中，其他处理日期和时间的模块还有

- datetime模块
- dateutil模块

## 参考

- [菜鸟 - 日期和时间](http://www.runoob.com/python3/python3-date-time.html)