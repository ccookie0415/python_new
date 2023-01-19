# lambda 함수

def triangle_area(b,h):
  return 0.5 * b * h
print(triangle_area(5,6))

triangle_area = lambda b, h : 0.5 * b * h
print(triangle_area(5,6))

'''
15.0
15.0
'''