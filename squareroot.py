'''
Filename: squareroot.py
Description: Program that takes a positive floating-point number as input and outputs an approximation of its square root.
Author: Finbar Dennehy

Resource references: 
    Newton method: https://en.wikipedia.org/wiki/Newton%27s_method
        "Newton's root finding algorithm: xₙ+₁ = xₙ - f(xₙ) / f'(xₙ) where xₙ is an approximation of the square root and xₙ+₁ is a better approximation.
        Finding the square root of a number a, that is to say the positive number x such that x² = a.
        We can rephrase as finding the zero of f(x) = x² - a. We have f'(x) = 2x.
        xₙ+₁ = xₙ - ( f(xₙ) / f'(xₙ) )    =   xₙ - ((xₙ² - a) / 2xₙ)    =   (xₙ + (a/xₙ)) / 2"
    Related Stack Overflow thread: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
    geeksforgeeks solutions: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
        During my research, I found three seperate ways of solving this issue:
        1. Continue refining the sqrt until xₙ+₁ = xₙ.
        2. Ask the user to define how many iterations of Newton's method should be used to approximate.
        3. Ask the user to set a tolerance level within which the answer is acceptable.
        I have chosen the third approach to solve.
'''

# prompt user to input psoitive floating point number
num = float(input("Please enter a positive number: "))

# Add some validation on the entered number to ensure it is a positive float
# This does not trap string input but prevents user from inputting negative or zero values.
while num <= 0:
    num = float(input("Please enter a positive number: "))

# prompt user to input a tolerance level (i.e. acceptable proximity of next iteration of Newton's method to previous approximation)
tolerance = float(input("Please enter the tolerance level: "))

# Define function called sqrt
def sqrt(num):
    # initial approximation (x₀) of the square root
    approx = num/2
    # Use Newton method to refine the next approximation (x₁) of the square root
    refine = (approx + (num/approx))/2
    # continue refining approximations (xₙ+₁) using Newton's method
    while abs(refine - approx) >= tolerance: # to continue refining wihtout tolerance level, this line is replaced with: while refine != approx:
        approx = refine 
        refine = (approx + (num/approx))/2
    # return approximation when it is within the tolerance level of last refinement.
    return approx

# print output of our square root fucntion, rounded to 1 decimal place (per output format provided in the example)
print(f"The square root of {num} is approx {sqrt(num):.1f}.")