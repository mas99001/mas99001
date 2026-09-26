import os
def clear_screen():
    # 'nt' means Windows, otherwise it's likely Linux or macOS
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
'''
class Employee:
    def __init__(self,id,age):
        self.id=id
        self.age=age 
    def printDetails(self):
        print(self.id)
        print(self.age)
emp1=Employee('E001',25)
emp1.printDetails()
emp1.age = 30
emp1.printDetails()
class Employee:
    def __init__(self,id,age):
        self.id=id
        self.age=age
    def printID(self):
        print(self.id)
    def printAge(abc):
        print(abc.age)
emp1=Employee('E001',30)
emp1.printAge()
###################
gv = 10
def calculate():
	global gv
	lv = 20
	print(f'Global variable: {gv}')
	print(f'Local variable: {lv}')
	area = gv * lv
	print(f'Area is: {area}')
	print(f'Global variable: {gv}')
	print(f'Local variable: {lv}')
calculate()
###################
def sort_by_length(strings):
    return sorted(strings, key=len)
words = ["apple", "kiwi", "banana", "fig", "elderberry"]
sorted_words = sort_by_length(words)
print("Original list:", words)
print("Sorted list by length:", sorted_words)
###################
def demonstrate_finally():
    try:
        print("1. Inside 'try' block — about to perform a bad operation...")
        # This will ALWAYS raise a ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"2. Inside 'except' block — caught error: {e}")
    finally:
        print("3. Inside 'finally' block — this code ALWAYS runs!")


# Run the function
demonstrate_finally()
###################
import logging
import traceback
# Setup basic logging
logging.basicConfig(
    filename="app_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
def divide_numbers(a, b):
    return a / b
def process_data():
    divide_numbers(10, 0)
try:
    process_data()
except ZeroDivisionError:
    # 1. Get the exception traceback as a string
    error_details = traceback.format_exc()

    # 2. Print a clean message to the user
    print("An error occurred during calculation. Details have been logged.")

    # 3. Log the full stack trace for developer debugging
    logging.error(f"Captured exception:\n{error_details}")
###################
filename="app_errors.log"
try:
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
        print('##### ALL WORDS #####')
        print(words)
        if not words:
            print('File is empty')
        longest = max(words, key=len)
        print('##### LONGEST WORD #####')
        print(longest)
except FileNotFoundError:
    print(f'{filename} is not available')
###################
a = int(input('Enter First number:'))
b = int(input('Enter Second number:'))
try:
	c = a/b
	print(f'{a} / {b} = {c}')
except ZeroDivisionError:
	print('Division by 0 is not defined')

'''
import json
file_name = 'data.json'
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print('Json file content:')
        print(json.dumps(data, indent=4))
except FileNotFoundError:
    print("File does not exist")
except json.JSONDecodeError:
    print(f'{file_name} contains invalid json content')
