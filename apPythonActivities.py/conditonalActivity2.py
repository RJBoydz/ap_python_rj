# 1. Write a function that uses a conditional statement. 
# Your function should return a message that will determine if
# class is over or not depending on the argument passed into your function.
# IF the time of class is greater than 11.30 (for AP section) or
# 1.00(for intro), your funcion should return a message saying 
# "class is over. Time to go". 
# ELSE if it is not, then your function should return a message saying
# "class is still in session."
# your function should also alow the user to put in the time. The time should be 
# formatted as a float. 

# keywords: function, conditional, statement, argument, flat
#clues: we need to send a message; if its time to or stay.

def letOut(leave_time):
   if leave_time>11.30:
      print('Class is over time t go')
   else:
      print('Class is not over')

letOut(12.10)

# 2. Write a function that uses a conditional statement. 
# your function should determine what type a pet a user has depeding on the data provided by the user
# passed into the functions argument. 
# IF the user types in "woof", the function should return a message saying that it is a dog.
# IF the user types in "meow", the function should return a message saying that it is a cat.
# ELSE, if it is none of the animal sounds the function should return a message saying it doesn't 
# know what the animal is. 

# keywords = functions, conditional, statement, argument, return,
# clues = we need to return a message depending on the condition.
# clues = the prompt tells us what to look for - animal sounds/words.

def animalYouWant(pet):
   pet = input('What sound is that?')
   if pet == 'woof':
      print('You get a dog')
   elif pet== "meow":
      print('you get cat')
   
   else:
      print('I do not know what you want?')   

animalYouWant()

# 3. Write a function that will take in a user name and height as parameters. 
# Your function should evaluate and determine if the user is tall in enough to get on a roller coster.
# IF the user is over 5.5, the function should return a custom message saying the user's name
# and a message "welcome please buckle up".
# ELSE if they they are not, return a message apologizing to the user saying they are not tall enough.

name =  input('What is your name?')
height = float(input('What is your age?'))

def AHeight(name, height):
   if height > 5.5:
      print('welcome, you should buckle up '+ name)
   else:
      print('Sorry but you are not tall enough to ride ' + name)

AHeight(name, height)