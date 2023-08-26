# Loops in python

# Using for loop to print out each element in a list

languages = ['English', 'French', 'German',
             'Japanese', 'Spanish', 'Italian', 'Chinese']
for language in languages:  # this line tells python to pull a name from the list languages, and associate it with the variable language
    # For every language in languages...
    print(language)
# Any lines of code after the for loop that are not indented are executed once without repetition.


# Using range() function

# It doesn't print 5, It actually prints only the numbers 1 through 4.
for value in range(1, 5):
    print(value)

# You could also pass range() only one argument, in this case it'll start the sequence of numbers at 0.

for numbers in range(8):
    print(numbers)

# Creating a list of numbers using range()
numbers = list(range(1, 6))
print(numbers)

# Passing a third argument to range()

# Python uses the third argument as a step size when generating numbers.
even_numbers = list(range(0, 50, 2))
odd_numbers = list(range(1, 50, 2))
print(even_numbers)
print(odd_numbers)

# Making a list of fist 10 square numbers

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Making a list of numbers divisible by 3 and 5

numbers_divisible_by_3 = []
numbers_divisible_by_5 = []
numbers_divisible_by_3and5 = []
for value in range(1, 50):
    if value % 3 == 0:
        numbers_divisible_by_3.append(value)
    if value % 5 == 0:
        numbers_divisible_by_5.append(value)
    if value % 3 == 0 and value % 5 == 0:
        numbers_divisible_by_3and5.append(value)
print(numbers_divisible_by_3)
print(numbers_divisible_by_5)
print(numbers_divisible_by_3and5)

cubes = []
for value in range(11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

# List comprehensions

squares = [value ** 2 for value in range(11)]
print(squares)

num2exponents = [2 ** value for value in range(11)]
print(num2exponents)

multiples_of3 = [value * 3 for value in range(1, 11)]
print(multiples_of3)

cubes = [value ** 3 for value in range(11)]
print(cubes)

# Slicing a list
# to make a slice, you specify the index of the first and last elements you want to work with.


Names = ['Tom', 'Joe', 'Pual', 'Micheal', 'John', 'Elizabeth']

# Python stops one item before the second index you specify.
# Without a starting, Python starts at the beginning of the list.
print(Names[0:3])
print(Names[:3])
print(Names[3:])
print(Names[::2])
print(Names[1::2])
print(Names[-3:])
print(Names[-1:])
print(Names[-1:-1])  # It is like the .reverse() function

index = 1
for name in Names:
    if index == 1:
        print(f'here is our {index}st audience, and his/her name is {name}.')
    if index == 2:
        print(f'here is our {index}nd audience, and his/her name is {name}.')
    if index == 3:
        print(f'here is our {index}rd audience, and his/her name is {name}.')
    if index >= 4:
        print(f'here is our {index}th audience, and his/her name is {name}.')
    index += 1


# Copy a list
# To copy a list, you can make a slice that includes the entire original list by ([:])

fruits = ['apple', 'orange', 'peach', 'banana', 'grape']
fruits_copy = fruits[:]

fruits.append('avocado')
fruits.remove('peach')
fruits_copy.append('blueberries')
fruits_copy.append('watermellon')

print(fruits)
print(fruits_copy)

fruits = fruits_copy

print(fruits_copy)
print(fruits)

# Using for loops to print specified items of a list
index = 0
for fruit in fruits:
    if index < 3:
        print(fruit)
    index += 1
