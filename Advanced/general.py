'''
s = 'Hello, World!'
print(s)
s = s.capitalize()
input("Press Enter to capitalize the string...")
print(s)

s = s.upper()
input("Press Enter to convert the string to uppercase...")
print(s)

s = s.lower()
input("Press Enter to convert the string to lowercase...")
print(s)

s = s.title()
input("Press Enter to convert the string to title case...")
print(s)

s = s.swapcase()
input("Press Enter to swap the case of the string...")
print(s)

s = s.replace('Hello', 'Hi')
input("Press Enter to replace 'Hello' with 'Hi'...")
print(s)

s = s.strip()
input("Press Enter to strip whitespace from the string...")
print(s)
'''

# Set operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(f'Set 1: {s1}')
print(f'Set 2: {s2}')

s3 = s1.intersection(s2)

print(f'Set 3: {s3}')

print('s1 symmetric difference:')
print(s1.symmetric_difference(s2))

