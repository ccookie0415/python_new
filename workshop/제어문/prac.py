number = int(input('자연수를 입력하세요 : '))
sum_ = 0

for i in range(1,number+1):
    if sum_ < 10000:
        sum_ = sum_ + i
        print(sum_)