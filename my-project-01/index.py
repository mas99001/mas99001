
'''
## Example to call Static methods from a class, here seld is not needed
from my_module import mylibstatic
a = int(input('Enter first number:'))
b = int(input('Enter first number:'))

# add
print(f'{a} + {b} is {mylibstatic.Calcs.add(a,b)}')

# subtract
print(f'{a} - {b} is {mylibstatic.Calcs.subtract(a,b)}')

# multiply
print(f'{a} * {b} is {mylibstatic.Calcs.multiply(a,b)}')

# divide
print(f'{a} / {b} is {mylibstatic.Calcs.divide(a,b):.2f}')

## 
'''
a = 5
b = 6 
print(a, b)
a, b = b, a 
print(a, b)
