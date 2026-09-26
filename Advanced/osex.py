'''
import os
print(os.getcwd())
print(os.listdir())
print(os.listdir('..'))
#import shutil
#import math
#help(math)
import pdb
x = 10
y = 20
z = x + y
a = [1, 2, 3, 4, 5]
pdb.set_trace()
z = z + a
print(z)
'''
''' Regular Expression example'''
text = 'The rain in Spain stays mainly in the plain. As there are no drains in the mountains, the plains are dry.'
import re
print('#### rain MATCHES')
pat ='rain'
match1 = re.search(pat, text)
print(match1)
print(match1.span())
print(text[match1.start():match1.end()])
print(text[match1.span()[0]])
print(text[match1.span()[1]-1])

print('#### pattern MATCHES')
pattern = r'\b\w+ain\w*\b'
matches = re.findall(pattern, text)
print(matches)
for match in matches:
    print(match)