# coding:utf-8

"""
    面向对象编程：
        把一组数据结构和处理它们的方法组成对象（object），
        把相同行为的对象归纳为类（class），
        通过类的封装（encapsulation）隐藏内部细节，
        通过继承（inheritance）实现类的特化（specialization）和泛化（generalization），
        通过多态（polymorphism）实现基于对象类型的动态分配。
"""


class Student(object):
    # __init__ 方法用于在创建对象时进行初始化操作
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self 是类函数中的必传参数，且必须放在第一个参数位置; self 是一个对象，它代表实例化的变量本身;

    def study(self, course_name):
        print(f'{self.name} 正在学习 {course_name}')

    def watch_movie(self):
        if self.age < 18:
            print(f'{self.name}, Black')
        else:
            print(f'{self.name}, Black Sun')


stu1 = Student('Alan', 22)
stu1.study('Python')  # Alan 正在学习 Python
stu1.watch_movie()  # Alan, Black Sun

stu2 = Student('Jack', 14)
stu2.study('JavaScript')  # Jack 正在学习 JavaScript
stu2.watch_movie()  # Jack, Black

"""
    私有的和公开的 属性、方法
"""


class Person:
    def __init__(self, id, name):
        self.__id = id
        self.name = name

    def __say1(self):
        print(f'id: {self.__id}, name: {self.name}')

    def say2(self):
        print(f'id: {self.__id}, name: {self.name}')


zhang = Person('123456', 'zhang')
print(zhang.name)  # zhang
# print(zhang.__id)  # # 'Person' object has no attribute '__id'
zhang.say2()  # id: 123456, name: zhang
# zhang.__say1()  # 'Person' object has no attribute '__say1'
