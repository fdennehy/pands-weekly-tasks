'''
Filename: weekday.py
Description: Program that outputs whether or not today is a weekday
Author: Finbar Dennehy
Resources:
    Official documentation on the datetime module: https://docs.python.org/3/library/datetime.html#module-datetime
        datetime class: https://docs.python.org/3/library/datetime.html#datetime.datetime
        today() function: https://docs.python.org/3/library/datetime.html#datetime.datetime.today
        weekday() function: https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
    Related thread on Stack Overflow: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
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