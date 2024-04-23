'''
Filename: collatz.py
Description: 
    A program that asks the user to input any positive integer and outputs the successive values of the following calculation.
    At each step, the next value is calculated by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
    The program ends if the current value is 1.
Author: Finbar Dennehy
Resources: I used the below two references to learn how to format the ouptut in the same way as presented in the example:
    https://docs.python.org/3/library/functions.html#print
    https://learnpython.com/blog/python-print-function/: 
    "If you want to print an iterable object like a list or an array, using a starred expression helps unpack the iterable and print it nicely"
'''

# create a list to which the number and resultant calculations will be appended
numbers = []

# prompt the user to enter a positive integer
number = int(input("Please enter a positive integer "))

# Add some validation on the entered number to ensure it is a positive integer (this will only capture 0 and negative whole numbers)
while number < 1:
    number = int(input("Please enter a positive integer "))

# Add logic for when the number is not at end state, i.e. when number does not equal 1.
while number != 1:
    numbers.append(number)
    if (number % 2) == 0:
        # no remainder => even number so we divide it by 2
        number = int(number/2)
    else:
        # otherwise we know it's an odd number (remainder of 1) so we multiply by 3 and add 1
        number = int((number*3)+1)
# print the numbers list using a starred expression and include final number (1)
print(*numbers, number)