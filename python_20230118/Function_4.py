a = 10
def func1():
    global a
    a = 3

print(a)
func1()
print(a)