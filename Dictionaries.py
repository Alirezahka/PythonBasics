# A dictionary in python is a collection of key-value pairs.
# A key's value can be a number, string, list, or even another dictionary.

Person_1 = {'Name': 'Armin', 'Last_name': 'Eshaghi',
            'Age': 25, 'Job': 'Artist', 'is_married': True}

# Accessing values in a dictionary

print(Person_1['Age'])
print(Person_1['Last_name'])

Person_1['is_graduated'] = False
Person_1['Country'] = 'USA'

# Redefine key-value pair to modify them as you wish
Person_1['is_married'] = False
print(type(Person_1), Person_1)

# Removing key-value pairs

del Person_1['Job']     # This key-value pair is removed permenently
print(Person_1)

Favorite_colour = {
    'Mohsen': 'Green',
    'Ehsan': 'Red',
    'Behzad': 'Blue',
    'Korosh': 'Gray',
    'Mohammad': 'Green',
}

# Using get() to access values
# You can use the get() method to set a default value that will be returned if the requested key doesn't exist.

polled_value = Favorite_colour.get(
    'Mohsen', "This person didn't take a poll.")

polled_value = Favorite_colour.get(
    'Farshid', "This person didn't take a poll.")

# The special value None means "no value exists."
polled_value = Favorite_colour.get('Hamidreza')

print(polled_value)

# Looping through dictionaries

for key, value in Favorite_colour.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for k, v in Person_1.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

for names in Favorite_colour.keys():   # This code would have exactly the same output if you omit keys() method
    print('\t', names)

for colours in Favorite_colour.values():
    print("\t\t", colours)

for colours in set(Favorite_colour.values()):
    print('\t', colours)

# Nested Dictionaries
