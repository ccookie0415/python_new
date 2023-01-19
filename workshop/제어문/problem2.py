# 가로로 출력하기
# 자연수 number를 입력 받아, 1부터 number까지의 수를 가로로 한칸씩 띄어 출력하시오

number = int(input('자연수를 입력하세요 : '))

for i in range(1, number+1):
    print(i, end=' ')