"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
from itertools import product


# remove the triple for x in z
# substitute for new function
def check_max_side(max_side):
    solutions = []
    for x, y, z in product(range(5, max_side), range(4, max_side), range(3, max_side)):
        if (x * x == y * y + z * z):
            solutions.append([x, y, z])
    return max(max(solutions))

# ask for input and print
max_side = input("What is the maximal length of the triangle side? Enter a number: ")
print("The longest side possible is " + str(check_max_side(int(max_side))))
