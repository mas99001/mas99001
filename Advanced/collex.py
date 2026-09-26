from collections import defaultdict, deque, namedtuple, Counter
'''an example of using collections module in python'''
'''defaultdict: A subclass of the built-in dict class that returns a default value for missing keys.'''
d = defaultdict(list)  # creates a defaultdict with a default value of an empty list
d['a'].append(1)
d['b'].append(2)
print(dict(d)) 
print(d['a'])  # returns [1] since 'a' is in the dictionary
print(d['b'])  # returns [2] since 'b' is in the dictionary
print(d[0])  # returns [0] since 0 is not in the dictionary
print(d[1])  # returns [0] since 1 is not in the dictionary
print(d['c'])  # returns [0] since 'c' is not in the dictionary
print(d)  # prints defaultdict(<class 'list'>, {'a': [1], 'b': [2], 'c': [0]})