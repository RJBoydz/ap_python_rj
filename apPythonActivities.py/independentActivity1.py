# read and review the following pages on Python lists. Use these to help you solve
# the questions. 

linkOne= 'https://www.w3schools.com/python/python_lists.asp'
linkTwo= 'https://afternerd.com/blog/python-lists-for-absolute-beginners/'

# Answers must be submitted by the end of class to recieve a grade. 
# when you submit your work, make sure your submit message is relevant and MAKES SENSE!

# REMEMBER TO USE WRITE CLEAN AND READABLE CODE!

# When ready, answer the following prompts, Good luck!

# 1.Create a simple list variable that contains 5 list items. It is up to you what will be in your list and what 
# data type they will be. 
# Some examples: favorite_atheletes, favorite_games, favorite_books, etc.
  
myfoodlist = ["Pizza", "Burger", "Cake", "Chicken", "Pop tarts"]
print(myfoodlist)

# What is a list
#A list is a way to store multiple values in a variable 

# 2. Find and print the specific item in each list based on their index in the list
# HINT you will need to use a python built-in function that specifically lets you find items in a Python list. 

# find and print index 3
zoo_animals = ['wolf','giraffe','hippo','eagle','parrot']

ZA = zoo_animals.index('eagle')

print(ZA) 

# find and print index 1
sports_on_tv =['hockey','football','baseball','soccer','racing']

SOT = sports_on_tv.index('football')

print(SOT)

# find and print index 0
random_numbers = [10,100,12123, 1394, 1]

RN = random_numbers.index(10)

print(RN)

# 3. Create a program that will only print out the odd numbers in this list. 

# HINT- part of solving this is that you will need to use the range() function. 

number_list= [1,2,3,4,5,6,7,8,9,10]

x = range(1,3,5,7,9)
for n in x:
  print(n)

# 4. You have been hired by amazon to be an engineer. Your first assignment is to fix their
# shopping cart function. Your goal is to create a line of code that will
# allow users to enter the item they want as a string value, and add it to the items that
# are already exist in the shopping_cart list variable. 
# Once the new item is entered, a list of all items in the cart should print out. 

# HINT - for this function you will need to use the append() function. 

shopping_cart = ['TV', 'pens', 'tool kit', 'computer', 'headphone','lamp']

added_item = input("what item would you like to add")

shopping_cart.append(added_item)

print(shopping_cart)

# Python list data type - a data type allows for storng multipule values in a variable.
# a Python lists uses [] square bracket for the values
number_list= [101, 10239, 10394, 10394] 
string_list=['kevin']
var_list=[number_list, string_list]

print(var_list)

apples = [2.00,'apple description']
tvDinner =[4.00, 'sphagetti and meatballs']
water =[3.00, '20 onces']

self_checkout_scanner=[apples, tvDinner, water]
print(len(self_checkout_scanner))

# type of container
# objects, stringer, other data types inside of list


# create a function that will add a new list item to a checkour cart
# the user should be able to enter the name of the items and the price
# your functuon should add the name of the item to the list of items
# and also add the price to the item to the total price of the items.
# including yhe price of the new item

list_of_items=['apple','organe', 'book', 'new item']
apple_price= 1.00
orange_price = 3.00
book_price = 10.00

def shopping():
  add = input('Would you like to add more to your shopping list')
  list_of_items.append(add)
  add_item= input('how much does it cost')
  print(list_of_items)
  print(list_of_items, + 'all will add up to ')
  all_price = (apple_price + orange_price + book_price + add_item)
  print(str(all_price))
  
  shopping():



