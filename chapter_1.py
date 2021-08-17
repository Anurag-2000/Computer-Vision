
# this file loads image and videos and web cam

import cv2 as cv
import numpy as np

# Load image using imread 

img = cv.imread(r'F:\\pycodes\\opencv\\pics\s.jpg')

# diplay the image 

cv.imshow('s', img)

cv.waitKey(0)  # This is used for to stop


# Load the video

frameWidth= 640
frameHight=480

cap = cv.VideoCapture('F:\pycodes\opencv\\vids\Watch Bungou Stray Dogs (Dub) Episode 4 at Gogoanime - Google Chrome 2021-05-15 14-12-36.mp4')

while True:
    isTrue, frame = cap.read()
    frame = cv.resize(frame, (frameWidth,frameHight))
    cv.imshow('video f by f', frame)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break


## For webcams

frameWidth= 640
frameHight=480

cap = cv.VideoCapture(0)

cap.set(3,frameWidth)
cap.set(3,frameHight)
cap.set(10,150)


while True:
    isTrue, frame = cap.read()
    frame = cv.resize(frame, (frameWidth,frameHight))
    cv.imshow('video f by f', frame)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break