import cv2 as cv

img = cv.imread('images\my.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1. Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

#Inverse Thresholding --> Just white instead of black and vice versa
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded', thresh_inv)

# 2. Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive THresholded', adaptive_thresh)

cv.waitKey(0)