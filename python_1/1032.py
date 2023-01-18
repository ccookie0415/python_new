n = int(input())
file_name = list(input())
# file_name2 = list(input())

for i in range(n-1):
    file_name2 = list(input())
    for j in range(len(file_name)):
        if file_name[j] != file_name2[j]:
            file_name[j] = '?'

print(''.join(file_name))