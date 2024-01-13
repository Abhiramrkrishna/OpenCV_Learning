import cv2 as cv
import numpy as np


# image = cv.imread('Cap3_1.jpg')
# cv.imshow('Calib', image)

## Creating Blank image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)

## 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

## 2. Draw a Rectangle
# cv.rectangle(blank,(0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# cv.rectangle(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

## 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50, (0,0,255), thickness = -1)
# cv.imshow('Circle', blank)

## 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness= 3)
# cv.imshow('Line', blank)

## 5. Write text
# cv.putText(blank,'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2 )
# cv.imshow('text', blank)

cv.waitKey(0)