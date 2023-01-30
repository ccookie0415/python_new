class Person:
    count = 0 # 클래스 변수
    def __init__(self,name): # 인스턴스 변수 설정
        self.name = name
        Person.count += 1
        
    @staticmethod
    def check_rich(money): # 스태틱은 cls, self, 사용 X
        return money > 10000
    
    
person1 = Person('아이유')
person2 = Person('이찬혁')
print(Person.check_rich(100000)) #True 스태틱은 클래스로 접근 가능
print(person1.check_rich(100000)) # True 스태틱은 인스턴스로 접근 가능