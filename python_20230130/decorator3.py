def add_print(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

@add_print
def print_hello():
    print("hello")
    
print_hello()