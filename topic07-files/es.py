# es.py
# program that reads in a text file and outputs the number of e's it contains.
# Author: Finbar Dennehy

'''
assumptions:
- ask is to count lower case e's from a text file, i.e. not to include upper case E's
- text file is saved in current working directory
- the text in the file is Unicode

Resources:
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
https://realpython.com/python-command-line-arguments/
https://youtu.be/rJCl7t3IIbA
https://docs.python.org/3/howto/unicode.html

From research, argparse might be a better module to use for error handling than below method
https://docs.python.org/3/library/argparse.html
https://www.youtube.com/watch?v=idq6rTYqvkY
'''

# import the internal Python modules sys and os
import sys
import os

# Store arguments in a variable, using slice to exclude argv[0] which is the program name
arguments = sys.argv[1:]

# Add error handling if no argument or more than one argument (len !=1) is passed on the command line
if len(arguments) != 1:
    print(f"ERROR: 1 argument expected, {len(arguments)} given!")
    # exit program
    sys.exit()

# Set FILENAME = argument that has been passed
FILENAME = sys.argv[1]

# Add error handling if a .txt file has not been passed by slicing last four chars from argument string and checking if they are ".txt"
if FILENAME[-4:] != ".txt":
    print(f"ERROR: .txt file expected")

# check if FILENAME exists
if os.path.exists(FILENAME):
    # if it exists, open in read mode and set unicode as encoding (error was thrown without this encoding when reading through my moby-dick.txt)
    with open(FILENAME, "r", encoding='utf-8') as f:
        # read in one line at a time, instead of reading in the whole file, in case we hit buffer sizes.  
        ecount = 0
        for data in f:
            # use count method to count occurrence of lowercase 'e's, and print the total
            # to include capital Es: + data.count('E')
            ecount += (data.count('e'))
        # Add error handling if filename does not exist in current working directory
    print(ecount)        
else:
    print(FILENAME, "does not exist")