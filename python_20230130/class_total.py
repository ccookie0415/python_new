class Myclass:
    
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'
    
    
# 인스턴스 메서드를 호출한 결과
    
obj = Myclass()
print(obj.method()) # ('instance method', <__main__.Myclass object at 0x000002A590ECFE20>)
print(Myclass.method(obj)) # ('instance method', <__main__.Myclass object at 0x000002A590ECFE20>)

# 클래스 자체에서 각 메서드를 호출하는 경우
#   - 인스턴스 메서드는 호출할 수 없음

print(Myclass.classmethod()) # ('class method', <class '__main__.Myclass'>)
print(Myclass.staticmethod()) # static method
# Myclass.method() # method() missing 1 required positional argument: 'self'

# 인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근할 수 있음

print(obj.classmethod())
print(Myclass.classmethod())
print(obj.staticmethod())