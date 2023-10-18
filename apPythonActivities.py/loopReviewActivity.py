# Create while loops for the following conditions


# 1. Create a security camera program that uses a while loop to detect if there is an
# object in site. 
camera1a = input("It there anything on camera 1A? ")

while camera1a = 'yes'
    print('object spotted')
    cam1a = input("Its it still there? ")
    break

while cam1a = 'yes'
    print('object spotted')
    print(cam1a)
    break

while camera1a = 'no' 
    print('good')
    break

while cam1a = 'no'
    print('good')
    break

# 2. Create a Printer Loop program that will continue to print copies of a document based on the number
# that the user inputs. 
printer = int(input('how many copy do you want? '))
while printer >= 0:
    print('copy made')
    printer += 1
    break
# 3. Create a Stop Light Loop that will change the light color based on different time intervals. 
# every 30 seconds the light should change between green and red. 

light = 1

while light < 30:
    print('green light')
    light +=1
    break

while light > 60:
    print('red flight')
    light -= 1
    break

# 3. BONUS: add an additional condition that will change the light to yellow for 5 seconds before the
# next light change. 
light = 1

while light < 35:
    print('green light')
    light +=1
    break

while light > 60:
    print('red flight')
    light -= 1
    break