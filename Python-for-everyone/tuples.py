# Lists work well for storing collections of items that CAN change throughout the life of a program.

# Tuples represent a list of items that cannot change(unchangeable). Python referes to values that cannot change as immutable, and immutable list is called a tuple.
# We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable)

# Defining a Tuple

empty_tuple = tuple()
empty_tuple = ()

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[2] = 300       It returns a type error, "tuple object does not support item assigment."


Name = ('Alireza', 'Hakimazar')
print(Name)

# If you want to define a tuple with one element, you need to include a trailing Comma!

my_unversity_major = ('nursing',)

# We can use len() method to get the length of a tuple

print(len(my_unversity_major))

# Accessing tuple items 

_tuple = ('item1', 'item2', 'item3', 'item4')

print(_tuple[0])
print(_tuple[2])
print(_tuple[3])
print(_tuple[-1])
print(_tuple[::2])
print(_tuple[::-1])

# Changing tuples into lists

_list = list(_tuple)
print('\tList: ', _list)

_tuple = tuple(_list)
print('\tTuple: ', _tuple)

# Checking an item in a tuple, using (in)
check_item2 = 'item2' in _tuple
print(check_item2)
check_item5 = 'item5' in _tuple
print(check_item5)

### _tuple[5] = 'item5'   'tuple' object does not support item assignment

# Joining tuples

tpl1 = ('item1', 'item2', 'item3', 'item4')
tpl2 = ('item5', 'item6', 'item8', 'item9')

tpl3 = tpl1 + tpl2
print(tpl3)

### It is not possible to remove a single item in a tuple, but it is possible to delete the tuple itself using _del_.

# Looping through all values in a tuple
for value in Name:
    print(value)

Name = ('Reza', 'Ahmadi') # If you want to change a value in a tuple, you can redefine the entire tuple.
for value in Name:
    print(value)

    