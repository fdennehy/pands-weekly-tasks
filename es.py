'''
Filename: es.py
Description: 
    A program that reads in a text file and outputs the number of e's it contains. 
    The program should take the filename from an argument on the command line.
    Error handling should be included for dealing with errors e.g.
        - No argument
        - Filename that does not exist
        - Filename provided is not a text file
# Author: Finbar Dennehy
'''

# import the internal Python modules sys
import sys

try:
    # Store arguments in a variable, using slice to exclude argv[0] which is the program name
    arguments = sys.argv[1:]
    
    # Raise exception if no argument or more than one argument (len !=1) is passed on the command line
    if len(arguments) != 1:
        raise IndexError(f"1 argument expected, {len(arguments)} given.")

    # Set filename = argument that has been passed
    filename = sys.argv[1]
    print(filename)

    # Raise exception if a .txt file has not been passed by slicing last four chars from argument string and checking if they are not ".txt"
    if filename[-4:] != ".txt":
        raise TypeError(f"{filename} expected to be passed as .txt file")

    #open in read mode and set unicode as encoding (error was thrown without this encoding when reading through my moby-dick.txt)
    with open(filename, "r") as f:
        # read in one line at a time, instead of reading in the whole file, in case we hit buffer sizes.
        ecount=0
        for data in f:
            # use count method to count occurrence of lowercase 'e's and uppercase 'E's, and print the total
            ecount += (data.count('e') + data.count('E'))
        print(ecount)

# Add runtime exception handling for when filename does not exist 
except FileNotFoundError as fnfe:
    print(f"file {filename} not found, please enter a file that exists")
    #print(f"FileNotFoundError: {fnfe}")



# Below was written pre week 9 lectures on error handling
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
            ecount += (data.count('e') + data.count('E'))
        # Add error handling if filename does not exist in current working directory
    print(ecount)        
else:
    print(FILENAME, "does not exist")
'''