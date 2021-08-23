import cv2 as cv
import numpy as np
from numpy.core.defchararray import upper


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
 

def empty(a):
    pass



path = 'F:\pycodes\computer Vision\lambo.png'
cv.namedWindow('trackbars')
cv.resizeWindow('trackbars',(640,240) )
cv.createTrackbar('Hue min', 'trackbars', 0, 179, empty)
cv.createTrackbar('Hue max', 'trackbars', 19, 179, empty)
cv.createTrackbar('Satu min', 'trackbars', 112, 255, empty)
cv.createTrackbar('Satu max', 'trackbars', 255, 255, empty)
cv.createTrackbar('Val min', 'trackbars', 160, 255, empty)
cv.createTrackbar('Val max', 'trackbars', 255, 255, empty)

img = cv.imread(path)


while True:

    imghsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos( 'Hue min', 'trackbars')
    h_max = cv.getTrackbarPos( 'Hue max', 'trackbars')
    s_min = cv.getTrackbarPos( 'Satu min', 'trackbars')
    s_max = cv.getTrackbarPos( 'Satu max', 'trackbars')
    v_min = cv.getTrackbarPos( 'Val min', 'trackbars')
    v_max = cv.getTrackbarPos( 'Val max', 'trackbars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
 
    lower = np.array([h_min, s_min,v_min])
    uppers = np.array([h_max, s_max,v_max])     
    masked = cv.inRange(imghsv,lower,uppers)

    final_img = cv.bitwise_and(img,img,mask=masked)

    # cv.imshow('lambo',img)
    # cv.imshow('lambohsv',imghsv)
    # cv.imshow('msked',masked)
    # cv.imshow('color detect',final_img)

    img_Stacked = stackImages(0.6, ([img,imghsv],[final_img,masked]))
    cv.imshow('final',img_Stacked)
    cv.waitKey(1)