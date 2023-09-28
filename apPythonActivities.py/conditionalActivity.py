# 1. What is the difference between 
# a parameter and an argument in a python function
'A parameter is the variable listed inside the parentheses in the function definition. '
'An argument is the value that are sent to the function when it is called.'

# 2. In your own words, describe what 
# a conditional statement (if/else) is 
'The if/else statement reads a block of code. if a specified part of the condition is true.'


# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )
a = 666
b = 99999
if b > a:
  print("b is greater than a")

# 3. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

frid = True

if frid == True:
   print("TIme to cook")
else:
   print('Is there food in the refridgerator ')

weekday= False


if weekday == False:
   print("Not ant food in the fridge, go out and buy some")
else:
   print("no food")

# 4. Create a function that checks the inventory of cereal for a store. 
# your function should parameter should accept an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".


inventory= True


if inventory == True:
   print("DO you need anymore cereal")
else:
   print("no we have enough")

def buyOFX(amountOfCereal):
  EnoughCereal = 10
  if amountOfCereal >= EnoughCereal:
     print("We have enough boxes")
  else:
    print('We will be good for now')

buyOFX(10)


