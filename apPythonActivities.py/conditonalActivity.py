# 1. What is the difference between 
# a parameter and an argument in a python function
'A parameter is the variable listed inside the parentheses in the function definition. '
'An argument is the value that are sent to the function when it is called.'

# 2. In your own words, describe what 
# a conditional statement (if/else) is 
'The if-else statement is used to execute both the true and false part of a given '
'function If the function is true, the if block code is executed and if the function '
' is false, the else block code is executed.'

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )
a = 666
b = 99999
if b > a:
  print("b is greater than a")
else:
   print('b is not greater than a')

# 3. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

# boolean as an argument in our fiction (value will either true or false)

def fridstuff(food):
   if food == True:
      print("TIme to cook")
   else:
         print('No food in the fridge')

fridstuff(True)


# 4. Create a function that checks the inventory of cereal for a store. 
# your function should parameter should accept an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

def inventory_of_cerel(amount):
   if amount > 10:
      print ('We have enogught cereal in stack')
else:
print('We do need more cereal')

print('______________________')
inventory_of_cerel(8)  