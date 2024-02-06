#say name
#author: Finbar Dennehy
#Prompt the user and read in two money amounts (in cent)
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# https://www.w3schools.com/python/ref_string_format.asp used for string formatting

amount1 = int(input("Enter amount1(in cent)"))
amount2 = int(input("Enter amount2(in cent)"))
total = (amount1 + amount2)/100
txt = "The sum of these is €{:.2f}"
print (txt.format(total))