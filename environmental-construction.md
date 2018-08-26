# 环境搭建

Python可应用于多平台包括 Linux 和 Mac OS X。

> *你可以通过终端窗口输入 `python` 命令来查看本地是否已经安装Python以及Python的安装版本。*

我是在 `Mac` 上学习 Python 的，而Mac自带了环境，可以看到默认安装了 `2.7` 的版本.

```bash
$ python

Python 2.7.10 (default, Oct  6 2017, 22:29:07)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

输入 `help()` 查看帮助

```bash
$ help()

Welcome to Python 2.7!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".
```

## 注意

> 我尝试去删除2.7版本的Python 但是没有删除成功！，下边 `Rootless` 操作没有尝试(担心出问题啊😅)。

由于Mac下的 `python2.7` 默认是安装在 `/System/Library/Frameworks/Python.framework` 目录下的。但是Mac有个 `Rootless` 机制，默认不允许直接在/System下作修改。所以要先关闭Rootless机制。

- 关闭Rootless机制的方法: 
关闭:   
1）.重启电脑, 重启过程中按住command+R, 进入恢复模式  
2）.打开terminal，键入: csrutil disable  
3）.重启电脑  

- 如果之后要再开启Rootless机制，方法如下：  
开启:   
1）.重启电脑, 重启过程中按住command+R, 进入恢复模式  
2）.打开terminal，键入: csrutil enable  
3）.重启电脑  

## 安装新版 Python

1. [官网下载](https://www.python.org/downloads/mac-osx/) 安装包  
    > 当前Mac最新版是 `3.7`  
2. 一路默认安装就好，安装完成后会在 `/Library/Frameworks/Python.framework` 目录下  
3. 安装完成后在控制台测试  

**注意 ⚠️** 我们输入的命令是 `python3` 而不是 `python`，这是因为我们保留了原有的 python 版本

```bash
$ python3
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Brew 安装

```bash
brew install python3
```

## 参考

- [Mac下升级python2.7到python3.6](https://blog.csdn.net/xummgg/article/details/69053334)