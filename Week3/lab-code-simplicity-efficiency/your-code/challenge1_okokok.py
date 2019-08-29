"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

import sys

# Just one print statement and better variable naming
print('''Welcome to this calculator!
      It can add and subtract whole numbers from zero to five''')
number1 = input('Please choose your first number (zero to five): ')
operation = input('What do you want to do? plus or minus: ')
number2 = input('Please choose your second number (zero to five): ')

# added new list of values
english_words = ['zero', 'one', 'two', 'three', 'four', 'five']
numbers = [0, 1, 2, 3, 4, 5]


# error handling
if number1 not in english_words or number2 not in english_words or \
        operation not in ['plus', 'minus']:
    sys.exit("Wrong input, please check your spelling.")

dict_numbers = dict(zip(english_words, numbers))

# remove long if function, define new function with equal resutl
def calculator(number1, number2, operation):
    if operation == 'plus':
        print(f"{number1} {operation} {number2} equals: "
              f"{dict_numbers[number1] + dict_numbers[number2]}")
    elif operation == 'minus':
        print(f"{number1} {operation} {number2} equals: "
              f"{dict_numbers[number1] - dict_numbers[number2]}")

# call function
calculator(number1, number2, operation)
print("Thanks for using this calculator, goodbye :)")
