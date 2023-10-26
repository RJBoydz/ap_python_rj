# String
# Boolean
# Integar
# Array - List

def store():
    item = input('What would you like from our store?')
    stuff = float(input('how much does it cost?'))
    member = input('Are you a member of the store club?')
    if member == 'yes':
        discount_25= stuff*.25
        print(stuff-discount_25)
    elif member == 'no':
        print('if you want to become member you will get a 10 percent discount')
    if member == 'yes':
       discount_10 = stuff*.10
       print(stuff- discount_10)
    else:
        print('heres your item price: '+ str(stuff))

store()    
            

