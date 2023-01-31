class Person:
    def __init__(self,name):
        self.name = name
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        
# 자식 클래스 - Professor
class Professor(Person):
    def talk(self):
        print(f'{self.name}일세.')
        
# 자식 클래스 - Student
class Student(Person):
    def talk(self):
        super().talk()
        print(f'저는 학생입니다.')
        
p1 = Professor('김교수')
p1.talk()

s1 = Student('이학생')
s1.talk()