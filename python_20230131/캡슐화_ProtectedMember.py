class Person:
    
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    def get_age(self):
        return self._age
    
p1 = Person('김싸피', 30)
print(p1.get_age())

print(p1._age)