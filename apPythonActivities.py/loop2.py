#i = 1
#while i < 6: 
#  print(i)
#  i += 1

#s = "malayalam"

#ans = palindrome
#def isPalindrome():
#    return s == s[::-1]
 
 
#if ans:
#    print("Yes")
#else:
#    print("No")

number=int(input("Enter any number :"))

temp=number

reverse_num=0

while(number>0):
    digit=number%10
    
    reverse_num=reverse_num*10+digit
    
    number=number//10

if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")

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