# Lists work well for storing collections of items that CAN change throughout the life of a program.

# Tuples represent a list of items that cannot change. Python referes to values that cannot change as immutable, and immutable list is called a tuple.

# Defining a Tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[2] = 300       It returns a type error, "tuple object does not support item assigment."


Name = ('Alireza', 'Hakimazar')
print(Name)

# If you want to define a tuple with one element, you need to include a trailing Comma!

my_unversity_major = ('nursing',)

# Looping through all values in a tuple
for value in Name:
    print(value)

Name = ('Reza', 'Ahmadi') # If you want to change a value in a tuple, you can redefine the entire tuple.
for value in Name:
    print(value)

    