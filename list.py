# Creating a list
# We use square brackets to indicate a list ([]).

List1 = [34, 12.53, "Yaser", (2,5)]

# Access individual Elements in a  list

print(List1[0])
print(List1[3])
print(List1[2])
print(List1[-1])       # It always gives you the last element 
last_item = len(List1) - 1
print(List1[last_item])
print(List1[-3])

# Changing, Adding and Removing elements

List1[3]= "Feresteh"
# List1[len(List1)] = "Behtash"     You can not append to a list with this value defining.
List1.append('Nastaran')    # Adding a new element to the END of a list
List1.append('Behtash')

List1.insert(3, 250000)     # Adding a new element at any position you specify.


tech_companies = ['asus', 'lenovo', 'macos', 'del', 'hp', 'sony', 'microsoft', 'msi', 'razor', 'samsung', 'xiaomi', 'huawei']

# delete an element from a list

del tech_companies[4]        # It removes HP at POSITION! 4

# pop() an element
popped_tech_companys = tech_companies.pop(2)

print(popped_tech_companys.title() + "'s Laptops are too enpensive.")

# Remove an element 
out_of_market = 'samsung'

tech_companies.remove(out_of_market)     # It is used mostly when you do not know the position of the value that you wanna delete from your list.
print(out_of_market.title() + ' Laptops are out of the market RN.')

print(tech_companies)


# Sorting a list 
Companies = ['asus', 'lenovo', 'macos','acer', 'del', 'hp', 'sony', 'microsoft', 'msi', 'razor', 'samsung', 'xiaomi', 'huawei']

Companies.sort()


print(Companies)
