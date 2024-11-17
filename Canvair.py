import cv2
import cv2 as cv
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath="Header"
myList=os.listdir(folderPath)
overlayList=[]
for imPath in myList:
    image=cv.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
header=overlayList[0]
drawColor=(0,0,255)
brushThickness=15
eThickness=100
xp,yp=0,0
currentColor=drawColor
imgCanvas=np.zeros((720,1280,3),np.uint8)

cap=cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector=htm.handDetector(detectionCon=0.85)


while True:
    success,img=cap.read()
    img = cv.flip(img, 1)

    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)

    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers=detector.fingersUp()

        if sum(fingers)==5:
            print("Erase")
            drawColor = (0, 0, 0)
            if xp==0 and yp==0:
                xp,yp=x2,y2
            cv.line(img,(xp,yp),(x2,y2),drawColor,eThickness)
            cv.line(imgCanvas,(xp,yp),(x2,y2),drawColor,eThickness)
            xp, yp = x2, y2
        elif fingers[1] and fingers[2]:
            drawColor=currentColor
            cv.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv.FILLED)
            print("Selection")
            if y1<100:
                if 650<x1<800:
                    header=overlayList[0]
                    drawColor=(0,0,255)
                    currentColor = drawColor
                elif 850<x1<900:
                    header=overlayList[1]
                    drawColor = (235, 206, 135)
                    currentColor = drawColor
                elif 950<x1<1050:
                    header=overlayList[2]
                    drawColor = (0, 255, 191)
                    currentColor = drawColor
                elif 1150<x1<1250:
                    header=overlayList[3]
                    drawColor = (204, 204, 204)
                    currentColor = drawColor
            cv.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv.FILLED)
            xp, yp=0,0

        elif fingers[1] and fingers[2]==False:
            drawColor=currentColor
            cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
            print("Drawing")
            if xp==0 and yp==0:
                xp,yp=x1,y1
            cv.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
            cv.line(imgCanvas,(xp,yp),(x1,y1),drawColor,brushThickness)
            xp, yp = x1, y1
    imgGray=cv.cvtColor(imgCanvas,cv.COLOR_BGR2GRAY)
    _,imgInv=cv2.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)
    imgInv=cv.cvtColor(imgInv,cv.COLOR_GRAY2BGR)
    img=cv.bitwise_and(img,imgInv)
    img=cv.bitwise_or(img,imgCanvas)

    img[0:100,0:1280]=header
    cv.imshow("Canvair",img)
    cv.imshow("Canvas", imgCanvas)
    cv.waitKey(1)