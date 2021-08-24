import cv2 as cv
import numpy as np
from numpy.lib.function_base import blackman


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
 
def getContour(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print (area)
        cv.drawContours(copyimg,cnt,-1,(0,0,0),3)
        perimeter  = cv.arcLength(cnt,True)
        # print(perimeter)
        corners = cv.approxPolyDP(cnt, 0.02*perimeter, True)
        print(len(corners))
        objCor = len(corners)
        x, y, w, h = cv.boundingRect(corners)

 
        if objCor ==3: objectType ="Tri"
        elif objCor == 4:
            aspRatio = w/float(h)
            if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
            else:objectType="Rectangle"
        elif objCor>4: objectType= "Circles"
        else:objectType="None"
        cv.rectangle(copyimg,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(copyimg,objectType,
        (x+(w//2)-10,y+(h//2)-10),cv.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)

path = 'F:\pycodes\computer Vision\shapes.png'

img = cv.imread(path)
copyimg = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (7,7), 1)
canny = cv.Canny(blur,50,50)
blank = np.zeros_like(img)
getContour(canny)


stacked = stackImages(0.6,([img,gray, blur],[copyimg,canny,blank]))
cv.imshow('fi', stacked)
cv.waitKey(0)
