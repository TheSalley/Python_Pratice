"""
    @property 装饰器
"""


class Person:
    # 限制Person 对象只能绑定某些属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 getter
    @property
    def name(self):
        return self._name

    # 访问器 getter
    @property
    def age(self):
        return self._age

    # 修改器 setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name} 正在玩五子棋')
        else:
            print(f'{self._name} 正在玩象棋')


zhang = Person('zhang', 12)
zhang.play()  # zhang 正在玩五子棋
zhang.age = 22
zhang.play()  # zhang 正在玩象棋
