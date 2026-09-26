'''
s1 = set()
for i in range(1, 11):
    s1.add(i)
print(f's1 is {s1}')

'''
''' demonstrate set operations '''
'''
s2 = s1.copy()
s2.remove(9)
s2.remove(10)

print(f's2 is {s2}')

print('difference of sets:')
s3 = s1.difference(s2)
print(f's3 is {s3}')

print('Intersction of sets')
s4 = s1.intersection(s2)
print(f's4 is {s4}')

print('Intersction_update of sets')
s2.intersection_update(s1)
print(f's2 is {s2}')

print('Union of sets')
s5 = set({1,2,3,4,5,6})
s6 = set({4,5,6,7,8,9})
print(f's5 is {s5}')
print(f's6 is {s6}')

print(f's5 union s6 is {s5.union(s6)}')
'''

d1 = {'k1':1, 'k2':2}
d2 = {k:v**2 for k,v in zip(['a','b'],range(2))}
print(d1)
print(d2)

l = [1,2,3,4]
print(f'l is {l}')
l.insert(1, "dfdsf")
print(f'l is {l}')
l.extend([7,8])
print(f'l is {l}')
l.pop()
print(f'l is {l}')
l.remove(1)
print(f'l is {l}')
l.remove(4)
print(f'l is {l}')
