'''
Filename: weekday.py
Description: Program that outputs whether or not today is a weekday
Author: Finbar Dennehy
    '''

# from the datetime module, import the datetime class:
from datetime import datetime

# use today() function to return today's date and weekday() function to return the day of the week as an integer, where Monday is 0 and Sunday is 6
today = datetime.today().weekday()

# check if it's Saturday or Sunday
if today > 4:
    print("It is the weekend, yay!")
# otherwise it's a weekday 
else: 
    print("Yes, unfortunately today is a weekday.")