# pands-weekly-tasks

## About This Project

This repository contains eight Python (.py) files, each relating to a specific topic covered as part of the Programming and Scripting module of the [HDip in Science in Computing in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics), ATU Galway. In addition to the eight Python files, the repository contains this README.md file, a .gitignore file, mobydick.txt and eee.txt files.
Below is a brief description of each file, including links to any resources that were referenced as well as any assumptions made:

## Files Description

1. *helloworld.py*\
Topic 1: Setup\
Description: Program that displays 'Hello World!' when it is run.

2. *bank.py*\
Topic 2: Statements\
Description: Program that prompts the user and reads in two amounts (in cent), adss the two amounts, and prints the sum in a human readable format with a euro sign and decimal point between the euro and cent of the amount.
Resource references:
    https://www.w3schools.com/python/ref_string_format.asp to understand the Python String format() Method in more detail.
    https://www.w3schools.com/python/python_string_formatting.asp to learn F_String is the preferred way of formatting strings to the above format() method.
    https://www.w3schools.com/python/python_operators.asp for more documentation on operators

3. *accounts.py*\
Topic 3: Variables\
Description: Program that reads in a 10-character account number and outputs the account numbers with only the last 4 digits showing (and the first 6 digits replaced with Xs). Program modified to deal with account numbers of any length.
Resource references: 
    https://stackoverflow.com/questions/509211/how-slicing-in-python-works for more information on slicing in python.
    https://stackoverflow.com/questions/38273353/how-to-repeat-individual-characters-in-strings-in-python to learn how to repeat letters through multiplication.

4. *collatz.py*\
Topic 4: Flow\
Description: Program that asks the user to input any positive integer and outputs the successive values of the following calculation:
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
The program ends if the current value is one.
Resource references: I used the below two references to learn how to format the ouptut in the same way as presented in the example:
    https://docs.python.org/3/library/functions.html#print
    https://learnpython.com/blog/python-print-function/: 
    "If you want to print an iterable object like a list or an array, using a starred expression helps unpack the iterable and print it nicely"

5. *weekday.py*\
Topic 5: Data Structures\
Description: Program that outputs whether or not today is a weekday.
Resource references:
    Official documentation on the datetime module: https://docs.python.org/3/library/datetime.html#module-datetime
        datetime class: https://docs.python.org/3/library/datetime.html#datetime.datetime
        today() function: https://docs.python.org/3/library/datetime.html#datetime.datetime.today
        weekday() function: https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
    Related thread on Stack Overflow: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date

6. *squareroot.py*\
Topic 6: Functions\
Description: Program that takes a positive floating-point number as input and outputs and approximation of its square root.
Resource references: 
    Newton method: https://en.wikipedia.org/wiki/Newton%27s_method
        "Newton's root finding algorithm: xₙ+₁ = xₙ - f(xₙ) / f'(xₙ) where xₙ is an approximation of the square root and xₙ+₁ is a better approximation.
        Finding the square root of a number a, that is to say the positive number x such that x² = a. 
        We can rephrase as finding the zero of f(x) = x² - a. We have f'(x) = 2x.
        xₙ+₁ = xₙ - ( f(xₙ) / f'(xₙ) )    =   xₙ - ((xₙ² - a) / 2xₙ)    =   (xₙ + (a/xₙ)) / 2"
    Related Stack Overflow thread: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
    geeksforgeeks solutions: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
        During my research, I found three seperate ways of solving this issue:
        1. Continue refining the sqrt until xₙ+₁ = xₙ.
        2. Ask the user to define how many iterations of Newton's method should be used to approximate.
        3. Ask the user to set a tolerance level within which the answer is acceptable. 
        I have chosen the third approach to solve.

7. *es.py*\
Topic 7: Files\
Description: Program that reads in a text file and outputs the number of e's it contains. The program takes the filename from an argument on the command line.
Resource references:
    Similar task: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
    Command line arguments: https://realpython.com/python-command-line-arguments/
    Tutorial video on running python scripts with command line arguments using sys.argv https://youtu.be/rJCl7t3IIbA
    Unicode: https://docs.python.org/3/howto/unicode.html
    From research, argparse might be another module to consider:
    https://docs.python.org/3/library/argparse.html
    https://www.youtube.com/watch?v=idq6rTYqvkY
    mobydick.txt file used for testing purposes sourced from: https://gist.github.com/StevenClontz/4445774
Assumptions:
- ask is to count number of e's in a text file: I assume this includes both lower case 'e's and upper case E's
- the text file is saved in the same working directory as this es.py file is saved

8. *plotask.py*\
Topic 8: Plots\
Description: Program that displays (1) a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2, and (2) a plot of the function $h(x)=x^3$ in the range 0 to 10, on one set of the axes.
Resource references:
    Numpy:
        https://realpython.com/tutorials/numpy/
        https://www.w3schools.com/python/numpy_intro.asp
        https://numpy.org/
        https://github.com/numpy/numpy
    Matplotlib:
        https://www.w3schools.com/python/matplotlib_intro.asp
        https://realpython.com/python-matplotlib-guide/

9. *README.md*\
Description: This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.

10. *.gitignore*\
Description: I have used the below github templates to create my .gitignore file:
    https://github.com/github/gitignore/blob/main/Python.gitignore
    https://github.com/github/gitignore/blob/main/Global/Windows.gitignore
    https://github.com/github/gitignore/blob/main/Global/macOS.gitignore

11. *eee.txt*\
Description: A text file I created to test my es.py program.

12. *.mobydick.txt*\
Description: A [text file of the novel Moby Dick](https://gist.github.com/StevenClontz/4445774) to test my es.py program.

## Use of this Project

This project may be useful to prospective students of the HDip in Science in Computing in Data Analytics course at ATU Galway, giving an indication of the content of the Programming and Scripting module and showcasing what can be achieved within a few weeks on the course. It may also be useful to other Python learners beginning their Data Analytics journey.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Git: [Download and Install Git](https://git-scm.com/)
- Python: [Download and Install Python](https://www.python.org/downloads/)

## Get Started 

Each file can be used independently. To run the files locally, clone the repository and then run the python files locally.

### Cloning the Repository

1. Open your terminal or command prompt. (I use [cmder](https://cmder.app/))
2. Navigate to the directory where you want to clone the repository.
3. Use the following command to clone the repository:
```bash
git clone https://github.com/fdennehy/pands-weekly-tasks
```

### Running Python Files

1. After cloning the repository, navigate into the repository's directory through the command prompt:
```bash
cd repository_name
```
Replace <repository_name> with the name of the directory under which you cloned the repository.

2. Once inside the repository's directory, you can run the .py scripts using the Python interpreter. For example, to run the helloworld.py script, use the following command:
```bash
python helloworld.py
```

Now you're ready to explore and use the Python files in the repository! 

## Get Help

Read the comments provided within the Python files and look up official Python documentation for further usage guidance.

## Contribute

Developers are welcome to fork this repo and continue to develop and expand upon it as they wish.

## Author

**Finbar Dennehy**

I'm currently undertaking the [HDip in Science in Computing in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics) on a part time basis at [ATU](https://www.atu.ie/)

I have over ten years' experience in capital markets consultancy and have spent the past few years working on software delivery and customer success. I am undertaking this program to better understand our clients, who are predominantly data scientists and data engineers.

## Acknowledgements

Special thanks to my lecturer on the Programming and Scripting module, Andrew Beatty, from whom I acquired the skills necessary to put this project together.
Now I'm going to stand up, strecth and grab myself a cup of tea!