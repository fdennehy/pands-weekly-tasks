# weekday.py
# Program that outputs whether or not today is a weekday
# Author: Finbar Dennehy

# import the datatime module: https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
import datetime

# use  today() function to return today's date and weekday() function to return the day of the week as an integer, where Monday is 0 and Sunday is 6
# today(): https://docs.python.org/3/library/datetime.html#datetime.datetime.today
# weekday(): https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
today = datetime.datetime.today().weekday()

# commenting out this check: print(today)

# check if it's a weekday
if today in (0,4):
    print("Yes, unfortunately today is a weekday")
# otherwise it's the weekend 
else: 
    print("It is the weekend, yay!")