import cv2 as cv
import numpy as np

img = cv.imread('Cap1_18.jpg')
cv.imshow('Image', img)

## Translation
# def translate(img, x, y):
#     transMAt = np.float32([[1,0,x], [0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMAt, dimensions)


## -x --> left
## -y --> up
## x --> right
## y --> down

# translatedImage = translate(img, -100, -100)
# cv.imshow('translated image', translatedImage)

## Rotation
# def rotate(img, angle, rotPoint=None):
#     (height,width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2,height//2)
#     rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions = (width,height)
#     return cv.warpAffine(img,rotMat, dimensions)

# rotated = rotate(img,-45)

# cv.imshow('rotated',rotated)

## Resizing
# resized = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
# cv.imshow('resized', resized)

## Flipping
# flip = cv.flip(resized,-1)
# cv.imshow('fliped', flip)

## Cropping
# cropped = resized[50:200, 200:400]
# cv.imshow('cropped', cropped)



cv.waitKey(0)