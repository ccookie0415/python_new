#filter

def odd(n):
		return n % 2
numbers = [1,2,3]
result = filter(odd, numbers)
print(result, type(result))
print(list(result))

'''
<filter object at 0x7f621c69a1f0> <class 'filter'>
[1, 3]
'''