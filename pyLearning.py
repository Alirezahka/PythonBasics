# Syntax highlighting: 

#editor way of showing recongnized functions and showing them in custom colors.
 
#Variables

Variable_name = 'Value' # String, integer, float, Boolean

# Variable rules to avoid name errors

# Variable names can contain only letter, numbers and underscores (_).
# a variable name cannot start with a number.
# Spaces are not allowed in declaring Variable names.
# Do not use Python preinstalled functions and keywords as a Variale names.
# Variable names should be short but descriptive.
# Be careful when using lowercase letter l and uppercase letter O. because they could be confused with the numbers 1, 0.


# Multiple Assignment
name, last_name, age, city = 'alireza', 'hakim azar', 20, 'Shahrekord'

# Comments
# Allows us to write notes in English within your programs. ignored by python.

# Traceback

# Strings is a series of characters
# Anything inside quotes is considered a string in python. You can use either single or double quotes around your strings.

# Variables inside Strings
# Sometimes we need to use a variable's value inside a string.
# Syntax error: remember you cannot use an apostrophe inside single quote. if so you have to use double quote to avoid syntax error.

# f-strings         the f stands for format

name = 'Alireza'
last_name = "Hakim azar"
age = 34

print(f"Hello I'm {name} and my last-name is {last_name}. I'm {age} years-old.")
print("I'm {} and I'm {} years-old.".format(name, age ))

# Whitespace 
#   \t means tab
#   \n means new line
# Exercise: print results shown below with \t and \n in a single string.            
# languages that I know:
#   Pyhton
#       HTML,CSS
#   JavaScript


# Numbers (integers) and opperations:

addition = 2 + 3
subtraction = 2 - 3
multiplication = 2 * 3
division = 2 / 3        # you'll always get a float for answer.
exponention = 2 ** 3
addition = 2 + 3
addition = 2 + 3

# Python supports the order of opperations 
# so in case you have specific precedence in mind, use parantheses to modify the order.
(2 + 3) * 4

# Floats: any number with a decimal point in Python.

total = 0.2 + 0.1 
print(total)  # it produces 0.300000000000004.
# just ignore it for now.

# Underscores in Numbers
my_earning = 20_000_000     # We use underscores to make large numbers more readable.
print(my_earning)   # Python prints only the digits.
