#def my_function():
 #   print("Twin mills is a hot wheels car made into a real car")

#my_function() 

#def my_function(blade):
#p-  print(blade + " glows")

#my_function("GOld")

#def my_function(fname, lname):
 # print(fname + " " + lname)

#my_function("Emil", "Refsnes")

#def welcome():
 # print("good morning welcome to class")
 # print("good afternoon")

# create aa function that will be used for a user's profile. Thus function should accept 3
# argument; a picture, can, location, when the code is ran, it should print out then values.

# we know we need to use pictue, ran. location. 
# we know need to print it out at same print.

def profleData():
location = input("where are you from")
name = input("whats your name?")
picture = input("upload a picture")

print("succes heres your proflies info")
print("name" + name)
print("location" + location)
print("picture" + picture)

#profleData()

# conditional statements
#Conditonal Statements are a tool that allows
# progras to control the outcome? excution of a programs
# depending on the scenario. We use the if and else keywords
# to excute a condtitional statement

sunIsOut = False

if sunIsOut == True:
   print("its day time")
else:
   print('night time ')

weekday= True


if weekday == True:
   print("you have school")
else:
   print("no school")

def buyOFX(moneyInAccount):
  priceOfGame = 70.00
  if moneyInAccount >= priceOfGame:
     print("you get game")
  else:
    print('you aint got to game')

buyOFX(70.00)