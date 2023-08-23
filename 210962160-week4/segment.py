import cv2 as cv
import numpy as np

# Load an image
image = cv.imread('./resources/fruits.png')

# Convert the image from BGR to HSV color space
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Define the lower and upper bounds of the color range you want to segment
lower_bound = np.array([20, 50, 50])  # Example lower HSV values for the color
upper_bound = np.array([40, 255, 255])  # Example upper HSV values for the color

# Create a mask using the inRange function
color_mask = cv.inRange(hsv_image, lower_bound, upper_bound)

# Apply the mask to the original image to get the segmented color region
segmented_image = cv.bitwise_and(image, image, mask=color_mask)

# Display the original and segmented images
cv.imshow('Original Image', image)
cv.imshow('Segmented Color Region', segmented_image)

cv.waitKey(0)
cv.destroyAllWindows()
