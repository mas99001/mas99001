def gensquares(limit=11):
    """Generate a list of squares of numbers from 0 to 9."""
    #return [i ** 2 for i in range(10)]
    for i in range(limit):
        yield i ** 2

p = gensquares()
'''Checking what the generator returns'''
print(p)
'''Iterating through the generator using next()'''
while True:
    try:
        #input("Press Enter to get the next square (or Ctrl+C to exit): ")
        print(next(p))
    except StopIteration:
        break
