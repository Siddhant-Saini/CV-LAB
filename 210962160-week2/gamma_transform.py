import cv2
import numpy as np

# Load the image
image_path = './resource/nature.jpeg'
image = cv2.imread(image_path)

# Define the gamma value (try different values like 0.5, 1.5, etc.)
gamma = 1.5

# Apply gamma correction
gamma_corrected = np.power(image/255.0, gamma) * 255.0

# Convert the gamma corrected image to the correct data type
gamma_corrected = np.uint8(gamma_corrected)

# Display the original and gamma corrected images
cv2.imshow('Original Image', image)
cv2.imshow(f'Gamma Corrected (Gamma = {gamma})', gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
