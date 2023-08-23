import cv2 as cv
import numpy as np

# Load an image
image = cv.imread('./resources/catex.png', cv.IMREAD_GRAYSCALE)

# Apply different thresholding methods
ret, binary_threshold = cv.threshold(image, 120, 255, cv.THRESH_BINARY)
ret, binary_inv_threshold = cv.threshold(image, 120, 255, cv.THRESH_BINARY_INV)
ret, trunc_threshold = cv.threshold(image, 120, 255, cv.THRESH_TRUNC)
ret, tozero_threshold = cv.threshold(image, 120, 255, cv.THRESH_TOZERO)
ret, tozero_inv_threshold = cv.threshold(image, 120, 255, cv.THRESH_TOZERO_INV)


stacked_images=np.hstack((image,binary_threshold,binary_inv_threshold,trunc_threshold,tozero_threshold,tozero_inv_threshold))
cv.imshow('Output',stacked_images)
cv.waitKey(0)
cv.destroyAllWindows()
