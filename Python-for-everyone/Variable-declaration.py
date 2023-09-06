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

# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b    # It always returns float as an answer
# Modulus(%): a % b
# Floor division(//): a // b    # (//) gives the answer without the remainder, or it floors the answer
# Exponentiation(**): a ** b

# Python supports the order of opperations 
# so in case you have specific precedence in mind, use parantheses to specify the order you have in your mind.
(2 + 3) * 4

# Floats: any number with a decimal point in Python.

total = 0.2 + 0.1 
print(total)  # it produces 0.300000000000004.
# just ignore it for now.

# Underscores in Numbers
my_earning = 20_000_000     # We use underscores to make large numbers more readable.
print(my_earning)   # Python prints only the digits.

# Logical operators
# pyhton uses _and_, _or_, _not_ as logical operators. Logical operators are used to combine conditional statements

print(3 > 2 and 4 > 5) # True-- because both statements are true
print(3 < 2 and 4 > 5) # False-- because one of the statements is false
print(3 < 2 and 4 < 5) # False-- because both statements are false
print('True and True:', True and True)

print(3 > 2 or 4 > 5) # True-- because both statements are true
print(3 < 2 or 4 > 5) # True-- because one of the statements is True
print(3 < 2 or 4 < 5) # False-- because both statements are false
print('True or False', True or False)

print(not 3 < 2) # True
print(not 4 > 5) # False
print(not True) # False
print(not not False) # False

### Exercises

# calculating the area of a circle
radius = int()
pi = 3.14

area_of_circle = pi * radius ** 2
print('Area of a circle: ', area_of_circle)

# Calculating the perimeter of a circle
perimeter_of_circle = 2 * pi * radius
print('The perimeter of a circle: ', perimeter_of_circle)

# Area of a rectangle
length = int()
width = int()

area_of_rectangle = length * width
print('Area of a rectangle: ', area_of_rectangle)

# Area of a triangle
base = int()
height = int()

area_of_triangle = 0.5 * base * height
print('Area of a triangle: ', area_of_triangle)

# Calculating the weight of an object
mass = int()
gravity = 9.807

weight = mass * gravity
print('The weight of an object in earth: ', weight)

# Calculating the weight of an object in Mars
gravity_in_mars = 3.71

weight_in_mars = mass * gravity_in_mars
print('The weight of an object in Mars: ', weight_in_mars)

## Calculating the volume of a sphere 
diameter = int()
radius = 0.5 * diameter

volume_of_sphere = (4/3) * pi * radius ** 3
print('The volume of a sphere: ', volume_of_sphere)