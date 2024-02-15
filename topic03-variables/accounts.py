# accounts.py
# program that reads in a 10 character account number and outputs the account number with only the last 4 digits displayed (and the first 6 digits replaced with Xs)
# Author: Finbar Dennehy

account_number = input("Please enter a 10 digit account number: ")

# hard code 6 Xs and concatenate with a splice of the last 4 digits of the account number string
redacted_account_number = "XXXXXX" + account_number[7:10]
print(redacted_account_number)


# Modify the program to deal with account numbers of any length
# https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
# Assumption that accout number >= 10 characters. First 6 digits are replaced with Xs 

account_number2 = input("Please enter your account number: ")
redacted_account_number2 = "XXXXXX" + (account_number2[-4:])
print(redacted_account_number2)