def print_family_name(*parents, **pets):
  print('아버지:',parents[0])
  print('어머니:',parents[1])
  if pets:
    print('반려동물들...')
    for title, name in pets.items():
      print('{} : {}'.format(title,name))

print_family_name('아부지','어무이',dog='멍멍이',cat='냥냥이')

'''
아버지: 아부지
어머니: 어무이
반려동물들...
dog : 멍멍이
cat : 냥냥이
'''