# 상속 - 상속 없이 구현하는 경우
# 학생/교수 정보를 나타내기 어려움

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')
        

s1 = Person('김학생', 23)
s1.talk()

p1 = Person('박교수', 49)
p1.talk()

s1.gpa = 4.5
p1.department = '컴퓨터공학과'