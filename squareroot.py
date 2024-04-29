'''
Filename: squareroot.py
Description: Program that takes a positive floating-point number as input and outputs an approximation of its square root.
Author: Finbar Dennehy
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