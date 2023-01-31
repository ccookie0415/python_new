# PublicMember

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = 30
        
# Person 클래스의 인스턴스인 p1은 이름(name)과 나이(age) 모두 접근 가능합니다.
p1 = Person('김싸피', 30)
print(p1.name)
print(p1.age)