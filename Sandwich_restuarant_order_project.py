from colorama import Fore, Back, Style
# even_numbers = []
# odd_numbers = []

# number = 0

# while number < 100:
#     number += 1
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)

# for enum in even_numbers:
#     print(enum)
# for onum in odd_numbers:
#     print("\t", onum)

# # numbers_divisible_by_5 = []
# # numbers_divisible_by_3 = []
# # numbers_divisible_by_11 = []
# # numbers_divisible_by_7 = []

# # numb = 0
# # while numb < 100:
# #     numb += 1
# #     if numb % 3 == 0:
# #         numbers_divisible_by_3.append(numb)
# #     if numb % 5 == 0:
# #         numbers_divisible_by_5.append(numb)
# #     if numb % 7 == 0:
# #         numbers_divisible_by_7.append(numb)
# #     if numb % 11 == 0:
# #         numbers_divisible_by_11.append(numb)

# # print(Fore.RED)
# # print(numbers_divisible_by_3)
# # print(Fore.BLUE)
# # print(numbers_divisible_by_7)
# # print(Fore.GREEN)
# # print(numbers_divisible_by_5)
# # print(Fore.MAGENTA)
# # print(numbers_divisible_by_11)
# # print(Style.RESET_ALL)


sandwich_menu = [
    'seafood sandwich',
    'roast beef sdandwich',
    'nutella sandwich',
    'grilled chicken sandwich',
    'egg sandwich',
    'prawn sandwich',
]

finished_sandwiches = []
dup_items = set()
uniq_orders = []

still_orders = True

while still_orders:
    ordered_sandwich = input('Order please: ')
    if ordered_sandwich.lower() in sandwich_menu:
        print(f'\tI made your {ordered_sandwich.title()}.')
        finished_sandwiches.append(ordered_sandwich.title())
        continue
    if ordered_sandwich.lower() not in sandwich_menu and ordered_sandwich != 'quit()':
        print("\tYour request doesn't exist, please order more curefully.")
        continue
    if ordered_sandwich == 'quit()':
        print('\n--- Made Sandwiches ---')
        while True:
            for dup_item in finished_sandwiches:
                uniq_orders.append(dup_item)
                dup_items.add(dup_item)
            for item in dup_items:
                count = finished_sandwiches.count(item)
                print(f"{count}* {item}")
            break
        total_sale = len(finished_sandwiches)
        print(f"\nToday total sales: {total_sale}")
    break
