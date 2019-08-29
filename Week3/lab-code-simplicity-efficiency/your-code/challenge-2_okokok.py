import random
import string
import sys

# new list for string lst and better variable naming
source_string = string.ascii_lowercase + string.digits

min_length = input('Enter minimum string length: ')
max_length = input('Enter maximum string length: ')
number_of_strings = input('How many random strings to generate? ')

# error handling
for i in (min_length, max_length, number_of_strings):
    if i.isnumeric() == False:
        sys.exit('Please input a number')

# simplification of functions one and two
def random_string_generator(length, source_string=source_string):
    string = ''
    for i in range(length):
        string += random.choice(source_string)
    return string
 


def batch_string_generator(min_length, max_length, number_of_strings):
    list_of_strings = []
    for i in range(number_of_strings):
        if min_length < max_length:
            string_length = random.choice(range(min_length, max_length))
        elif min_length == max_length:
            string_length = min_length
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        list_of_strings.append(random_string_generator(string_length))
    return list_of_strings

# print
print(f"Here is your random list of random strings: "
      f"{batch_string_generator(int(min_length), int(max_length), int(number_of_strings))}")
