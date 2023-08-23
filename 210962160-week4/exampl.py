import cv2 as cv
import numpy as np

image = cv.imread('./resources/catex.png')

img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, thresh1 = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

# Create a stacked image using numpy's hstack function
stacked_images = np.hstack((thresh1, thresh2, thresh3, thresh4, thresh5))

# Display the stacked image
cv.imshow('Stacked Thresholded Images', stacked_images)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
