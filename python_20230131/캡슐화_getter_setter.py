class Person:
    
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For SSAFY')
            return
        
        self._age = new_age
        
# 인스턴스를 만들어서 나이에 접근하면 정상적으로 출력됩니다.
p1 = Person(20)
print(p1.age)

# p1 인스턴스의 나이를 다른 값으로 바꿔도 정상적으로 반영됩니다.
p1.age =33
print(p1.age)

# setter 함수에는 "나이가 19살 이하면 안된다"는 조건문이 하나 걸려있습니다.
# 따라서 나이를 19살 이하인 값으로 변경하게 되면 오류가 발생합니다.
p1.age = 19