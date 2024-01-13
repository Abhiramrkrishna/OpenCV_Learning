import cv2 as cv
#import numpy as np


img = cv.imread('my.jpg')
cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# # Laplacian
# lap = cv.Laplacian(gray, cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined Sobel', combined_sobel)
cv.waitKey(0)