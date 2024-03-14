# squareroot.py
# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Finbar Dennehy

''' 
Newton method: https://en.wikipedia.org/wiki/Newton%27s_method
Newton's root finding algorithm: xₙ+₁ = xₙ - f(xₙ) / f'(xₙ) where xₙ is an approximation of the square root and xₙ+₁ is a better approximation.
"Finding the square root of a number a, that is to say the positive number x such that x² = a. 
We can rephrase as finding the zero of f(x) = x² - a. We have f'(x) = 2x."
xₙ+₁ = xₙ - ( f(xₙ) / f'(xₙ) )    =   xₙ - ((xₙ² - a) / 2xₙ)    =   (xₙ + (a/xₙ)) / 2
'''

# import the decimal module so that we can use decimals instead of floats
from decimal import Decimal

# prompt user input as type float and convert to decimal for future operations
num = Decimal(float(input("Please enter a positive number: ")))

# Add some validation on the entered number to ensure it is a positive float
# This does not error trap string input but prevents user from inputting negative or zero values.
while num <= 0:
    num = float(input("Please enter a positive number: "))

# Define function called sqrt
def sqrt(num):
    # initial approximation (x₀) of the square root
    approx = num/2
    # Use Newton method to refine the next approximation (x₁) of the square root
    refine = (approx + (num/approx))/2
    # continue refining approximations (xₙ+₁) using Newton's method
    while refine != approx:
        approx = refine 
        refine = (approx + (num/approx))/2
    # return approximation when the root is solved by the algorhitm, when it can't be refined any more, i.e. when refine = approx.
    return approx

# print output of our square root fucntion, rounded to 1 decimal place (per output format provided in the example)
print(f"The square root of {num} is approx {sqrt(num):.1f}")