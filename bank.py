'''
Filename: bank.py
Description: A program that:
    1) prompts the user and reads in two money amounts (in cent)
    2) Adds the two amounts
    3) Prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
Author: Finbar Dennehy
Resources: 
    I used https://www.w3schools.com/python/ref_string_format.asp to understand the Python String format() Method in more detail.
    I used https://www.w3schools.com/python/python_string_formatting.asp to learn F_String is the preferred way of formatting strings to the above format() method.
'''

# Ask the User to enter first amount and store as an integer (instead of default type str).
amount1 = int(input("Enter amount1(in cent)"))

# Ask the User to enter second amount and store as an integer (instead of default type str).
amount2 = int(input("Enter amount2(in cent)"))

# Sum up the two amounts and divide by 100 to convert from cent to euro. The division operation makes the total variable a floating type.
total = (amount1 + amount2)/100

# Print a hard-coded string and use F_String to format the total variable to 2 decimal places.
print(f"The sum of these is €{total:.2f}")