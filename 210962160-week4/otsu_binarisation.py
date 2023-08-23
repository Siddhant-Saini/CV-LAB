import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load an image in grayscale
image = cv.imread('./resources/catinmountain.jpg', cv.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
ret, otsu_threshold = cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Display the original and Otsu thresholded images
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.imshow(otsu_threshold, cmap='gray')
plt.title('Otsu Binarization')

plt.show()
