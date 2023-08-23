import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load an image
image = cv.imread('./resources/catinmountain.jpg')

# Convert image to floating point type
image_float = np.float32(image)

# Reshape the image to a 2D array of pixels
pixels = image_float.reshape((-1, 3))

# Define the criteria for k-means
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Specify the number of clusters (k)
k = 10

# Perform k-means clustering
_, labels, centers = cv.kmeans(pixels, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

# Convert the centers back to 8-bit integer values
centers = np.uint8(centers)

# Map the labels to the centers
segmented_image = centers[labels.flatten()]

# Reshape the segmented image back to its original shape
segmented_image = segmented_image.reshape(image.shape)

# Display the original and segmented images
plt.subplot(121)
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(122)
plt.imshow(cv.cvtColor(segmented_image, cv.COLOR_BGR2RGB))
plt.title('Segmented Image')

plt.show()
