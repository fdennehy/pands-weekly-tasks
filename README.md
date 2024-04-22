# pands-weekly-tasks

## About This Project

This repository contains eight Python (.py) files, each relating to a specific topic covered as part of the Programming and Scripting module of the [HDip in Science in Computing in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics), ATU Galway. In addition to the eight Python files, the repository contains this README.md file and a .gitignore file. Below is a brief description of each file:

## Files Description

1. *helloworld.py*\
Topic 1: Setup\
Description: Program that displays 'Hello World!' when it is run.

2. *bank.py*\
Topic 2: Statements\
Description: Program that prompts the user and reads in two amounts (in cent), adss the two amounts, and prints the sum in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

3. *accounts.py*\
Topic 3: Variables\
Description: Program that reads in a 10-character account number and outputs the account numbers with only the last 4 digits showing (and the first 6 digits replaced with Xs). Program modified to deal with account numbers of any length.

4. *collatz.py*\
Topic 4: Flow\
Description: Program that asks the user to input any positive integer and outputs the successive values of the following calculation:
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
The program ends if the current value is one.

5. *weekday.py*\
Topic 5: Data Structures\
Description: Program that outputs whether or not today is a weekday.

6. *squareroot.py*\
Topic 6: Functions\
Description: Program that takes a positive floating-point number as input and outputs and approximation of its square root.

7. *es.py*\
Topic 7: Files\
Description: Program that reads in a text file and outputs the number of e'2 it contains. The program takes the filename from an argument on the command line.

8. *plotask.py*\
Topic 8: Plots\
Description: Program that displays:
- a histogram of a normal distribution of 1000 values with a mean of 5 and a standard deviation of 2,
- plot of the function $h(x)=x^3$ in the range 0 to 10,\
on one set of the axes.

9. *README.md*\
Description: This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.

10. *.gitignore*\
Description: I have used the below github templates to create my .gitignore file:
https://github.com/github/gitignore/blob/main/Python.gitignore
https://github.com/github/gitignore/blob/main/Global/Windows.gitignore
https://github.com/github/gitignore/blob/main/Global/macOS.gitignore

## Use of this Project

This project may be useful to prospective students of the HDip in Science in Computing in Data Analytics course at ATU Galway, giving an indication of the content of the Programming and Scripting module and showcasing what can be achieved within a few weeks on the course. It may also be useful to other Python learners beginning their Data Analytics journey.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Git: [Download and Install Git](https://git-scm.com/)
- Python: [Download and Install Python](https://www.python.org/downloads/)

## Get Started 

Each file can be used independently. To run the files locally, clone the repository and then run the python files locally.

### Cloning the Repository

1. Open your terminal or command prompt (I use [cmder](https://cmder.app/))
2. Navigate to the directory where you want to clone the repository.
3. Use the following command to clone the repository:
```bash
git clone https://github.com/fdennehy/pands-weekly-tasks
```

### Running Python Files

1. After cloning the repository, navigate into the repository's directory using the 'cd' command:
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