'''
Filename: accounts.py
Description: A program that reads in a 10 character account number and outputs the account number with only the last 4 digits displayed (and the first 6 digits replaced with Xs)
Author: Finbar Dennehy
'''
# Modified program below.
'''
Modify the program to deal with account numbers of any length
Assumptions: 
    Account numbers with 4 or less digits will be fully dispayed (no redaction)
    For account numbers with more than 4 digits, the number of digits redacted will be the length of the account number - 4.
        E.g. 1st digit redacted for 5 digit account number, First 2 digits redacted for 6 digit account number, etc. 
'''

# Ask user to enter their account number.
account_number = input("Please enter your account number: ")

# Calculate how many Xs are required by subtracting 4 from the length of the account number. Create a string of this number of Xs and assign to redacted variable.
redacted = (len(account_number) - 4)*'X'

# Concatenate Xs (if account > 4 digits) and the last 4 digits of the account number 
redacted_account_number = redacted + (account_number[-4:])

# Print the redacted account number.
print(redacted_account_number)

# Original program below
'''
# Ask user to enter 10 digit account number, defaulting to type str.
account_number2 = input("Please enter a 10 digit account number: ")

# Hard code 6 Xs and concatenate with a slice of the last 4 digits of the account number string.
redacted_account_number2 = "XXXXXX" + account_number2[7:10]

# Print the redacted account number.
print(redacted_account_number2)
'''