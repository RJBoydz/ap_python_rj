# 1. Explain what built-in functions are? Then describe and proivde 
# code examples of three (3) built-in functions we learned about in class.

#pre-defined functions that come bundled with Python and can be used directly
# in a Python program without importing external libraries.
# Float: a function into converts values into floating point numbers. 
x = float(3)
print(x)

# String: Strings in python are surrounded by either single quotation marks,
# or double quotation marks.
a = "Hello"
print(a)

# The Integer function converts the specified value into an integer number.
T = int("12")
print(T)

# 2. provide three (3) code examples of how to use you will need to use one (1) of each of the following
# operators in your examples: assignment operator, the logical operator and comparison operator.

#If: The if statement executes some code if one condition is true.
c = 33
D = 200
if c > D:
  print("b is greater than a")

# Elif: keyword is pythons way of saying. 
# "if the previous conditions were not true, then try this condition"
l = 33
j = 33
if l > j:
  print("l is greater than j")
elif l == j:
  print("l and j are equal")

#Else:keyword catches anything which isn't caught by the preceding conditions.
u = 200
i = 33
if u > i:
  print("i is greater than u")
elif u == i:
  print("u and i are equal")
else:
  print("u is greater than i")


# 3.Create function that will loop through the list of numbers provide below and multiply each number by 3
list_of_numbers=[100,20,34,45,75,9,60]
my_new_list = [i * 3 for i in list_of_numbers]

print(my_new_list)



# 4. Create a function that will check is a user's input is a palendrome.
# HINT1: a palendrome is a word that reads the same way backwards as it does forwards
# HINT 2: you will need to use a loop.
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)  
string = input("Enter the string: ")
print("Method 1")
status= check_palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")
