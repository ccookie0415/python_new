# 학생(Student)을 표현하기 위한 클래스를 생성합니다.

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
    def study(self):
        self.gpa += 0.1
        
# 교수(Professor)를 표현하기 위한 클래스를 생성합니다.

class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
    def teach(self):
        self.age += 1
        
class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')