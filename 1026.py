# 1026
# n개, a는 재배열 가능 b는 재배열 불가
# a[i] * b[i] + a[i+1] * b[i+1] = 최소가 되도록 코드 구성


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

result = 0

for i in range(len(a)):
    c = int(a[i]) * int(b[i])
    result += c

print(result)