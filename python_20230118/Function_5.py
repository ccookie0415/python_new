x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x)
    
func1()
print(x)