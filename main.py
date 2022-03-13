# Prints the raw axis readings in micro-Tesla

from PiicoDev_QMC6310 import PiicoDev_QMC6310
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

magSensor = PiicoDev_QMC6310() # Initialise the sensor (defaults to range=3000uT)
magSensor.setRange(1200)
display = create_PiicoDev_SSD1306()

def magList(): # Outputs a list of the mag data [X,Y,Z]
    data = magSensor.read()
    return [int(data['x']),int(data['y']),int(data['z'])]

def listComp(listOne,listTwo,operator = 0): #Operator represents what comparision happens
    #0 = greater than
    # 1 = Less than
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
            else:
                print('Operator not defined')
        return returnList
    else:
        print('Lists not equal length')

def initRotation(): #Figures out which *two* axis the magnet is rotating about - PLANAR ROTATION ONLY
    flag = 0
    print('please rotate magnet ')
    #Allow a function to be an input so a system can be self calibrated
    maxData = magList()
    minData = magList()
    limVars = 
    while flag < 4:
        newData = magList()
        compLarger = listComp(maxData,newData,0)
        compSmaller = listComp(maxData,newData,1)
        if 1 in compLarger:
            maxData[compList.index(1)] = newData[compList.index(1)]
        if 1 in compSmaller:
            minData[compList.index(1)] = newData[compList.index(1)]
            
def magAngleInit():
    cutoff = 0.3*sum(abs(item) for item in magList())
    expectedMax = 0.9*sum(abs(item) for item in magList())
    return [expectedMax, cutoff]
    
            
def magAngle():
    

lis = [5,4,3,2,1]
liss = [1,2,3,4,5]

print(listGreEq(liss,lis,0))
# while True:
#     print(magList())             # Print the data
#     sleep_ms(20)
