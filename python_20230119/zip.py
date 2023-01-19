# zip(*iterables)

girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(pair, type(pair))
print(list(pair))

'''
<zip object at 0x7f6213023280> <class 'zip'>
[('jane', 'justin'), ('ashley', 'eric')]
'''