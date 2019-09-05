# -*- coding: utf-8 -*-

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self._gender = gender
    def get_gender(self):
        return self._gender
    def set_gender(self, gender):
        self._gender = gender


bart = Student('Bart', 'male')
print(bart.get_gender())
