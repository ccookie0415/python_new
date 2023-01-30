class cal:
    
    def __init__(self,num):
        self.num = num
           
    count = 0
    
    def calc(self):
        cal.count = 0
        while True:
            if self.num == 1:
                return cal.count
            
            elif self.num % 2 == 0:
                self.num = self.num / 2
                cal.count += 1
                
            elif self.num % 2 == 1:
                self.num = self.num * 3 + 1
                cal.count += 1
                
            if cal.count >= 500:
                return -1
                
    def collatz(self):
        print(cal.calc(self))
        
num1 = cal(6)
num1.collatz()

num2 = cal(16)
num2.collatz()

num3 = cal(27)
num3.collatz()

num4 = cal(626331)
num4.collatz()