import one

print('TWO.PY:TOP LEVEL!')
one.func()
if __name__ == '__main__':
    print('TWO.PY:RUNNING AS SCRIPT!') 
else:
    print('TWO.PY:RUNNING AS MODULE!')