# def add_and_mul(a,b):
#     return a+b, a*b

# result = add_and_mul(3,4)
# print(result)



# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s 입니다" % nick)

# a = say_nick('야호')
 
# print(a)

# def say_myself(name, age, man=True):
#     print("나의 이름은 %s" %name)
#     print("나이는 %d살" %age)
#     if man:
#         print("남자")
#     else :
#         print("여자")
        
# b = say_myself('임혜진',27,False)
# print(b)

a = 1
def vartest():
    global a
    a =  a + 1
     
vartest()
print(a)