# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Create a Boolean variable named x
x = True
print(x)                           # True
# Create an integer variable named y
y = 5
print(type(y))                      # <class 'int'>
# Create a float variable named z
z = 10.50
print(type(z))                      # <class 'float'>
# Create a string variable names s
s = "10"
print(type(s))                       # <class 'str'>
# Convert the int variable to float
y2 = float(y)
print(type(y2))                      # <class 'float'>
# Can we convert the str to int ?
s2 = int(s)
print(type(s2))                      # <class 'int'>
# Create a list of numbers from 1 to 5
listName = [1,2,3,4,5]
print(type(listName))                 # <class 'list'>
# Create a tuple from 10 to 15
tupleName = (10,11,12,13,14,15)
print(type(tupleName))                 #<class 'tuple'>
# Create a tuple from 10 to 15
tupleName = (10,11,12,13,14,15)
print(type(tupleName))                 #<class 'tuple'>
# Convert the list to tuple
tupleName2 = (listName)                # listName = [1,2,3,4,5]
print(type(tupleName2))                # (1, 2, 3, 4, 5)
# Create a dict of 3 values
info = {"jihad":31 , "karem" :25 , "mustafa":24}     # <class 'dict'>
print(type(info))

 1) Python is interpreted or compiled ?
# Both
#  run the code via interpreter
# Compiles and converts the program to bytecode, and directly bytecode is loaded in system memory.
# Then compiled bytecode interpreted from memory to execute it.

# 2) What is the differences between low level & high level ?
# * High-level languages:

# + Feature abstraction
# + Are closer to human languages, and are more readable
# + Do not deal with memory management
# + Examples include: Java, Python, Ruby, and C#

# * Low-level languages::

# + Do not feature abstraction
# + Are readable by machines, and are not close to human language
# + Involve memory management
# Examples include assembly language and machine code


