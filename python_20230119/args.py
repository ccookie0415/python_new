def sum_all(*numbers):
		result = 0
		for number in numbers:
				result += number
		return result

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))

'''
6
21
'''