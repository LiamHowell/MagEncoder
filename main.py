# Prints the raw axis readings in micro-Tesla

from PiicoDev_QMC6310 import PiicoDev_QMC6310
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
import math

magSensor = PiicoDev_QMC6310() # Initialise the sensor (defaults to range=3000uT)
magSensor.setRange(1200)
display = create_PiicoDev_SSD1306()

def magList(): # Outputs a list of the mag data [X,Y,Z]
    data = magSensor.read()
    return [int(data['x']),int(data['y']),int(data['z'])]

def listComp(listOne,listTwo,operator = 0): #Operator represents what comparision happens
    #0 = greater than
    # 1 = Less than
    # 2 = equal to
    if len(listOne) == len(listTwo):
        returnList = [] # a 1 indicates that the index of listOne is larger in that location
        for i in range(len(listOne)):
            if operator == 0:
                if listOne[i] > listTwo[i]:
                    returnList.append(1)
                else:
                    returnList.append(0)
            elif operator == 1:
                if listOne[i] < listTwo[i]:
                    returnList.append(1)
                else:
                    returnList.append(0)
            elif operator == 2:
                if listOne[i] == listTwo[i]:
                    returnList.append(1)
                else:
                    returnList.append(0)
            else:
                print('Operator not defined')
        return returnList
    else:
        print('Lists not equal length')

def initRotation(delay = 200): #Figures out which *two* axis the magnet is rotating about - PLANAR ROTATION ONLY
    flag = 0
    print('please rotate magnet ')
    #Allow a function to be an input so a system can be self calibrated
    maxData = magList()
    minData = maxData.copy()
    limVars = magAngleInit(maxData)
    update = 0
    while flag < 4:
        sleep_ms(delay)
        newData = magList()
        compLarger = listComp(newData,maxData,0)
        compSmaller = listComp(newData,minData,1)
        if 1 in compLarger:
            maxData[compLarger.index(1)] = newData[compLarger.index(1)]
            update += 1
        if 1 in compSmaller:
            minData[compSmaller.index(1)] = newData[compSmaller.index(1)]
            update += 1
        
        if sum(listComp(3*[limVars[0]],maxData,1)) == 2 and sum(listComp(3*[-limVars[0]],minData,0)) == 2:
            if listComp(3*[limVars[0]],maxData,1) == listComp(3*[-limVars[0]],minData,0):
                print('Calibrated')
                sleep_ms(delay)
                return listComp(3*[limVars[0]],maxData,1)

            
def magAngleInit(magData = None):
    if magData == None:
        magData = magList()
    cutoff = int(0.3*sum(abs(item) for item in magData))
    expectedMax = int(0.65*sum(abs(item) for item in magData))
    return [expectedMax, cutoff]
    
            
def magAngle(caliData):
    magData = magList()
    magData.pop(caliData.index(0))
    if magData[1] == 0:
        magData[1] = 1
    ang = math.atan(magData[0]/magData[1])
    if magData[0] >0 and magData[1] <0:
        ang = math.pi + ang
    if magData[0] <0 and magData[1] <0:
        ang = math.pi + ang
    if magData[0] <0 and magData[1] >0:
        ang = ang + math.pi*2
    return math.degrees(ang)

    

# lis = [5,4,3,2,1]  #old data - max/min
# liss = [1,2,3,4,5] #new data
# 
# lissTest = listComp(liss,lis,1)

def drawCompass(heading):
    rads = radians(heading) # convert heading to radians and offset by 180 degrees (to account for y increasing down the display)
    length = 25 # compass needle length (in pixels) from centre
    
    # Convert polar coordinates (length, angle) to cartesian coordinates (x,y) for plotting on display. Offset the coordinates by half the screen width/height to draw from the centre - rather than the top-left of the display.
    x = int( length * sin(rads) + WIDTH/2 )
    y = int( length * cos(rads) + HEIGHT/2 )
    
    # Plot the compass on the display
    display.fill(0)
    display.line(64, 32, x, y, 1) # draw the compass needle
    display.circ(x,y,4)                     # put a north-indicator on the end
    display.text(str(heading),100,57)       # show the heading in the bottom-right corner
    display.show()





display.text("Please rotate", 0,0,1)
display.text("magnet :D",0,15,1)
display.show()
caliData = initRotation()
display.fill(0)
display.show()
while True:
#     
#     ang = magAngle(caliData)
#     display.arc(64,32,15,0,ang,0.5)
#     display.show()
#     sleep_ms(200)
#     display.fill(0)
#     display.show()
#     
    heading = magAngle(caliData)

    drawCompass(heading)
    print(heading)

    sleep_ms(100)
