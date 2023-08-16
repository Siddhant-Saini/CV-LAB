
import cv2
import numpy as np


# Load the input and reference images
input_image_path = './resource/nature.jpeg'
reference_image_path = './resource/dog.jpg'

input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread(reference_image_path, cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization on the input image
equalized_input = cv2.equalizeHist(input_image)

# Compute the histograms of the equalized input and reference images
equalized_input_hist = cv2.calcHist([equalized_input], [0], None, [256], [0, 256])
reference_hist = cv2.calcHist([reference_image], [0], None, [256], [0, 256])

# Compute the cumulative histograms
equalized_input_cdf = np.cumsum(equalized_input_hist) / np.sum(equalized_input_hist)
reference_cdf = np.cumsum(reference_hist) / np.sum(reference_hist)

# Create a lookup table for histogram specification
lookup_table = np.zeros(256, dtype=np.uint8)
for i in range(256):
    j = 255
    while reference_cdf[j] > equalized_input_cdf[i] and j > 0:
        j -= 1
    lookup_table[i] = j

# Apply the lookup table to the equalized input image
specified_image = lookup_table[equalized_input]

# Display the input, reference, equalized input, and specified images
cv2.imshow('Input Image', input_image)
cv2.imshow('Reference Image', reference_image)
cv2.imshow('Equalized Input Image', equalized_input)
cv2.imshow('Specified Image', specified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
