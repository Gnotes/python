# 类的属性与方法

- `类` 属性
    ```python
    class T:
        props = None # 这个就是类属性
    ```
- `实例` 属性
    ```python
        t = T()
        t.props = 1 # 实例属性
    ```

注： 通过实例访问属性时，如果 **实例对象没有找到**，会 “向上查找” `类属性`

----

- `类方法`
    ```python
    class T:
        @classmethod
        def method(cls): # cls: Python 自动添加当前类引用
            pass

    T.method()
    ```
- `实例方法`
    ```python
    class T:
        def method(self):
            pass

    t = T()
    t.method()
    ```
- `静态方法`
    ```python
    class T:
        @staticmethod
        def method():
            pass

    T.method()
    ```