class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    def get_age(self):
        return self.__age
    
# 인스턴스를 만들고 get_age 메서드를 활용하여 호출할 수 있습니다.
# 실행시켜 확인해봅시다.

p1 = Person('김싸피', 30)
print(p1.get_age())

# __age에 직접 접근이 불가능합니다.
# print(p1.__age)