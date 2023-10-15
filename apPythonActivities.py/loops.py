#i= 0
#while i <= 100:
 #   print(i) 
#    i+=1

#alarmTime = float(input('what time is it'))

#(=) assign a variable to a value
#(==) compare and evaluate if the values are the same

#while alarmTime ==8.00:
#    print('time to wake up')
#    print('waiting for time to go.')


#a= len(shopping_cart)
#print(a)

exampleList=[1,2,3,4,5,6,7,8]
b=len(exampleList)
print(b)

#len() # counts the number of items in a list.
shopping_cart = ['apple', 'orange', 'bread', 'meat']

i = 0
while i < len(shopping_cart):
    print(shopping_cart[i])
    i+=1

# while loop = repeat some code forever,
# until the condition its looking is net.

time = [1,2,3,4,5]
i = 0
while i < len(time):
    print('you cannot park here during the ' + str(time[i]) + ' o clock')
    i+=1
print('you can park now because it is 5pm')