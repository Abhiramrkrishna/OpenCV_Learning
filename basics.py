import cv2 as cv

img = cv.imread('my.jpg')

## Rescaling
def RescaleCalib(img, scale = 0.75):
    width = int(img.shape[0] * scale)
    Height = int(img.shape[1] * scale)
    dimensions = (width, Height)
    return cv.resize(img, dimensions, interpolation= cv.INTER_AREA )


resizedimage = RescaleCalib(img)
cv.imshow('Calib', resizedimage)


##Converting to greyscale
# gray = cv.cvtColor(resizedimage, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)


## Blurring
# blur = cv.GaussianBlur(resizedimage, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blurred', blur)

## Edge cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

## Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

## Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

## Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

## Cropping
# cropped = resizedimage[50:200, 200:400]
# cv.imshow('cropped', cropped)

cv.waitKey(0)