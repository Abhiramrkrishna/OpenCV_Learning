import cv2 as cv
import numpy as np

img = cv.imread('my.jpg')
cv.imshow('Image', img)

# Blank variable for the purpose of drawing over the contours(dimension same as og img)
# blank = np.zeros(img.shape, dtype= 'uint8')
# cv.imshow('Blank', blank)

## Step1 - Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)

## Blurring to reduce contours
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blurred', blur)

## Step2 - Canny edge detector
# canny = cv.Canny(blur, 125, 175, cv.THRESH_BINARY)
# cv.imshow('Canny Edges', canny)
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

## Step2 - Instead of cannying we can use threshold
# ret, thresh = cv.threshold(gray, 175, 255, cv.THRESH_BINARY)
# cv.imshow('Thresholded image', thresh)
# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# print(f'{len(contours)} contour(s) found..!')

## To draw contours
# cv.drawContours(blank, contours, -1, (0,0,255), 1)
# cv.imshow('Contours Drawn', blank)

cv.waitKey(0)