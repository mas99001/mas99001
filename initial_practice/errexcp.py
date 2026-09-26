
while True:
    try:
        x = int(input("Please enter a number: "))
        print(f'{x}**2 = {x**2}')
        #break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
    else:
        print("No exception occurred.")
        break
    finally:
        print("Executing finally clause.")