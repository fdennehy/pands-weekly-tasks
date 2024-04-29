'''
Filename: bank.py
Description: A program that:
    1) prompts the user and reads in two money amounts (in cent)
    2) Adds the two amounts
    3) Prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
Author: Finbar Dennehy
    '''

# Ask the User to enter first amount and store as an integer (instead of default type str).
amount1 = int(input("Enter amount1(in cent)"))

# Ask the User to enter second amount and store as an integer (instead of default type str).
amount2 = int(input("Enter amount2(in cent)"))

# Sum up the two amounts to get total amount (in cent)
total = amount1 + amount2

# Instead of dividing total by 100 (which would introduce floating point number), seperate euro and cent using other operators to returns ints:
euro = total // 100 # Floor Division: rounds down to nearest integer
cent = total % 100 # Modulus: returns the remainder of the division

# Print the answer in human readable format by creating an f-string with placeholders for euro and cent amounts, with € sign and decimal point between euro and cent.
print(f"The sum of these is €{euro}.{cent}")

# With floating point numbers solution below:
'''
# Sum up the two amounts and divide by 100 to convert from cent to euro. The division operation makes the total variable a floating type.
total = (amount1 + amount2)/100

# Create an f-string to format the total variable to 2 decimal places.
print(f"The sum of these is €{total:.2f}")
'''