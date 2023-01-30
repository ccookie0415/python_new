class Fourcal():
    
    def __init__(self, first,second):
        self.first = first
        self.second = second
        
    def setdata(self,first,second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
    
    
a = Fourcal(4,2)
b = Fourcal(3,2)


# print(a.first)
# print(a.second)

class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
print(a.pow())
print(a.add())