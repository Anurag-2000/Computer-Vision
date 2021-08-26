import cv2 as cv
import numpy as np

def preprocessing(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(img,(5,5),1) 
    canny  = cv.Canny(blur,200,200)
    kernel = np.ones((5,5))
    imgdialated = cv.dilate(canny,kernel,iterations=2)
    Threshold = cv.erode(imgdialated,kernel,iterations=1)
    return Threshold

def getContour(img):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        # print (area)
        if area>5000:
            cv.drawContours(imgContour,cnt,-1,(0,0,0),3)
            perimeter  = cv.arcLength(cnt,True)
            # print(perimeter)
            corners = cv.approxPolyDP(cnt, 0.02*perimeter, True)
            if area> maxArea and len(corners) == 4:
                biggest =corners
                maxArea = area
    return biggest

def getWarp(img,biggest):
    pass





frameWidth= 640
frameHight=480

cap = cv.VideoCapture(0)

cap.set(3,frameWidth)
cap.set(3,frameHight)
cap.set(10,150)


while True:
    isTrue, frame = cap.read() 
    frame = cv.resize(frame, (frameWidth,frameHight))
    imgContour = frame.copy()
    imgThresh = preprocessing(frame)
    cv.imshow('video f by f', imgThresh)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break