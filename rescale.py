import cv2 as cv

## Rescaling Image
# img = cv.imread('Cap1_0.jpg')
# cv.imshow('Calibration', img)

def rescaleFrame(frame, scale = 0.2):
    width = int(frame.shape[1] * scale)
    Height = int(frame.shape[0] * scale)

    dimensions = (width,Height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# resized_image = rescaleFrame(img)
# cv.imshow('image resized', resized_image)

## Rescaling videos
capture = cv.VideoCapture('Videos\trial.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Zoom', frame)
    cv.imshow('Zoom resize', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)