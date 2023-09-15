# List is a collection of items which is ordered and modifiable, and allows duplicate members
# We use square brackets to indicate a list

List1 = [34, 12.53, "Yaser", (2, 5)]

empty_list = list()  # Creating an empty list with list built-in function
empty_lst = []

# Access individual Elements in a  list

print(List1[0])
print(List1[3])
print(List1[2])
print(List1[-1])       # It always gives you the last element
last_item = len(List1) - 1
print(List1[last_item])
print(List1[-3])

# Changing, Adding and Removing elements

List1[3] = "Feresteh"
# List1[len(List1)] = "Behtash"     You can not append to a list with this value defining.
List1.append('Nastaran')    # Adding a new element to the END of a list
List1.append('Behtash')

List1.insert(3, 250000)     # Adding a new element at any position you specify.


tech_companies = ['asus', 'lenovo', 'macos', 'del', 'hp', 'sony',
                  'microsoft', 'msi', 'razor', 'samsung', 'xiaomi', 'huawei']

# delete an element from a list

del tech_companies[4]        # It removes HP at POSITION! 4

# pop() an element
popped_tech_companys = tech_companies.pop(2)

print(popped_tech_companys.title() + "'s Laptops are too enpensive.")

# Remove an element
out_of_market = 'samsung'

# It is used mostly when you do not know the position of the value that you wanna delete from your list.
tech_companies.remove(out_of_market)
print(out_of_market.title() + ' Laptops are out of the market RN.')

print(tech_companies)


# Sorting a list Permanently/Temporarily
Companies = ['asus', 'lenovo', 'macos', 'acer', 'del', 'hp', 'sony',
             'microsoft', 'msi', 'razor', 'samsung', 'xiaomi', 'huawei']

# Temporarily

# to maintain the original order of a list we use sorted() istead of sort()
print(sorted(Companies))

# Permanently

Companies.sort()  # alphabetical order
Companies.sort(reverse=True)  # reverse alphabetical order

print(Companies)

# Reverse the order of a list
car_companies = ['Bmw', 'Lexus', 'toyota', 'porsche', 'Benz']

car_companies.reverse()
print(car_companies)

# another way to do that
print(car_companies[::-1])

# Finding the Length of a List

print(len(car_companies))   # It returms the number of items that presents in a list.

# Slicing items from a list

car_companies = ['Bmw', 'Lexus', 'toyota', 'porsche', 'Benz']

print(car_companies[0:])
print(car_companies[1:4]) # It excludes the first and last item
print(car_companies[::2]) # It ecludes odd index number items



books_wish_list = ['Secret', 'Compound effect', 'Unlimited memory', 'Atomic habits']
print(books_wish_list)

read_books = []

while books_wish_list:
    current_book = books_wish_list.pop()
    read_books.append(current_book)

print(read_books)
print(books_wish_list)