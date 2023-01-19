# 재귀함수 : 팩토리얼을 반복문으로 작성

def fact(n):
  result = 1
  while n > 1:
    result *= n
    n -= 1
  return result

print(fact(4))

'''
24
'''