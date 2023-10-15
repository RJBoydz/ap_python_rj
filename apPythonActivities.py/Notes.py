#loop is a piece of code that iterates, or loops over a statement as long as the condition is true  
#NOt a conditional statment, a conditional statement goes inside a loop

# loop example
cereal_intentory = 10
cereal_sold= str(input('how much cereal did qw sell today?'))

#if cereal_soild >= cereal_intentory:
#    print('we need to order more cereal')
#else:
#    print('we still have cereal boxes in the back')

#cereal_intentory = 10
while cereal_sold >= cereal_intentory:
    print('we need to order more cereal')
    cereal_sold += 1

# LOOPS

#the iterator: 
# this is a variable thats acts as the starting points for our loop.

# The condition
# This will be what we are evaluting. Depending on what we set our condition to it will continue to loop 
# until the condition is met

# The incrementor
# This will be the counter, or the numer of times your loop will run. We use the += assignemt operator.

# Bonus the breaker
# This keyword is used when we want to create a statement or piece of mode for when the loop ends.

# While loop will keep going, and never end.

# simple Loop 

i= 0
while i <= 10:
    print(i) 
    i+1=1

# collon symbol
# pattern for code instruction inside of functions.
def functions():
    #some code here

if 0 > 1:
    # some code here

while 0>1:

#While(loop functions) combined wiht True & False

alarmTime = float(input('what time is it'))

#(=) assign a variable to a value
#(==) compare and evaluate if the values are the same

while alarmTime ==8.00:
    print('time to wake up')
    print('waiting for time to go.')

shopping_cart = ['apple', 'orange', 'bread', 'meat']
i=0
while shopping_cart[i] >=4:
    print(shopping_cart[i])
    shopping_cart[i]+=1


