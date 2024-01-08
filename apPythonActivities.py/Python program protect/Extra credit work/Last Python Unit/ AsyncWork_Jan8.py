# 1. List and explain three 3 reasons why programmers write documentation.
#Clarity and Understanding, Maintenance and Updates, quality and process control


# 2.Describe three (3) negative outcomes that could happen if a programmer has bad or no documentation.
#Poor documentation makes it difficult for developers to understand the product and slows down the development process.
# if you put out your documentation to fast, someone could steal your ideas.
# if you do a documentation, but change your code later, than the documentation won't match.


# 3. You have been hired as an engineer at a local grocery store a program the will remove apples from users 
#shopping cart. Create a function that when a users shopping cart list is passed into the function it will remove 
#the "apples" and return the new updated shopping list. You can choose to solve this problem in anyway you see fit.

def store():
    food = ['apple, chicken, carrots']
    Stuff = input('What kind of food do you want.')+ food
    if food == 'apple':
        print("No we won't have more apples.")
    else:  
        print("Sorry we don't have that")
store() 

# 4. Once you have completed the coding segment for question number 3, please clearly explain how you went 
#about solving this problem and why you chose to solve to solve it that way.

#I put the whole function in a def, and use put on the variables in string, and use a if or else statement.