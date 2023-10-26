def cameraScanner():
    objectSpotted = bool(input('Is ther an objects here?'))
    while objectSpotted == False:
        print('scanning area')
        objectSpotted = bool(input('Is ther an objects here?'))
    print('OBJECT DETECTED! SOUNDING ALARM!!!!')

#cameraScanner()

def rjFunction():
    camera1a = input("Is there anything on camera 1A? ")
    while camera1a == 'yes':
        print('object spotted')
        cam1a = input("Is it still there? ")
        continue 
            
#rjFunction()

def makaiFunction():
    cameraVision = 0
    while cameraSensativeity == True:
        print('no one in sight')
        peopleInsight = input('is there any one in sight. 1 if yes if no')
        if sightSensativtiy == 'yes':
            break


def printerFunction():
    printer = 0
    numberOfDocs= int(input('how many copies do you want to print?:'))
    while printer <= numberOfDocs:
        print('print document.exe')
        printer+=1

#RIGHT ANSWER
def stopLight():
    # every 30 (seconds) change the light color
    stop = 'red light'
    go = 'green light'
    i= 0
    while i < 120:
        print('count up:' +str(i))
        i+=1
        if i==30:
            print(stop)
        elif i==60:
            print(go)
        elif i==90:
            print(stop)
        elif i==120:
            print(go)

stopLight()