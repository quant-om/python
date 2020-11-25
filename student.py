"""
__author__ = 'quant-om'

This the implementation of Student class
"""


class Student:

    def __init__(self, st_id, st_name):
        self.st_id = st_id
        self.st_name = st_name
        self.gender = None
        self.st_class = None
        self.marks = {}
        self.school = None

    def set_gender(self, gnd):
        self.gender = gnd

    def set_class(self, class_st):
        self.st_class = class_st

    def set_school(self, sch_name):
        self.school = sch_name

    def set_marks(self, sub_name, marks_obt):
        self.marks[sub_name] = marks_obt

    def mod_st_name(self, st_new_name):
        self.st_name = st_new_name

    def get_school(self):
        return self.school

    def get_stname(self):
        return self.st_name

    def get_st_id(self):
        return self.st_id

    def get_st_gender(self):
        return self.gender

    def get_class(self):
        return self.st_class

    def get_marks(self):
        return self.marks

    def get_totalmarks(self):
        total = 0
        for key in self.marks:
            total = total + self.marks[key]

        return total

    def __repr__(self):
        total = 0
        for key in self.marks:
            total = total + self.marks[key]
        return f"==============================\n" \
               f"       Student Record...\n" \
               f"==============================\n" \
               f"Name       :{self.st_name}\n" \
               f"ID         :{self.st_id}\n" \
               f"Gender     :{self.gender}\n" \
               f"Class      :{self.st_class}\n" \
               f"School     :{self.school}\n" \
               f"Total Marks:{total}\n"




student1 = Student(101, 'quant-om')
student2 = Student(102, 'quant-om123')

print(f"Student={student1}")
name = student1.get_stname()
print(f"Student name = {name}")
student1.set_gender("male")
student1.set_class(10)
student1.set_school("DPS")
student1.set_marks("Mathematics", 77)
student1.set_marks("Science", 89)
student1.set_marks("Social", 70)

name = student1.get_school()
print(f"School name = {name}")

name = student1.get_st_gender()
print(f"School name = {name}")

marks = student1.get_marks()
print(f"Student marks = {marks}")

marks = student1.get_totalmarks()
print(f"Student total marks = {marks}")

print(student1)
