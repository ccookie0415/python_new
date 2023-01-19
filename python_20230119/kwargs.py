def print_family_name(father,mother, *pets):
    print(f'아버지 : {father}')
    print(f'어머니 : {mother}')
    print('반려동물들...')
    for name in pets:
        print(f'반려동물: {name}')

print_family_name('아부지','어무니','멍멍이','냥냥이')

'''
아버지 : 아부지
어머니 : 어무니
반려동물들...
반려동물: 멍멍이
반려동물: 냥냥이
'''