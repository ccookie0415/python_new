a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a,b,c)
    local(300)
    print(a,b,c)
enclosed()
print(a,b)