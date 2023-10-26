# 1. In your own words, describe what a for loop is?
#With the for loop you can execute a set of statements, once for each item in a list, cars, set etc.,

# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 

#For Loop
#For loop iterates over a sequence, but the while loop doesn't.
# For Loop will repeat a condition a finite amount times.
#code example
def caser()
cars = ["camaro", "challenger", "ferrari"]
for x in cars:
  print(x)

#While Loop.
#The differences is A while loop's condtion statment must be true, a for loop doesn't need that
# A while loop will run the condition an indefinite amount of time if it is true.
#cide example
i = 0@!!while i < 9:
  print(i)
  i += 1


# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']
for letter in names:
  print(letter[0])
  if letter[0]=='R':
    print(letter)