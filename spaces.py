import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images\my.jpg')
cv.imshow('Image', img)

# # RBG Image
# plt.imshow(img)
# plt.show()

# # BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# # BGR to l*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# # BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

# #  HSV to BGR
# hsvtobgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('HSVTOBGR', hsvtobgr)


cv.waitKey(0)