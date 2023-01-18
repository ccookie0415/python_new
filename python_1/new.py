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

# for i in range(n):
#     max_b = b.index(max(b))
#     s += a[i]*b[max_b]
#     b.pop(max_b)
# print(s)

