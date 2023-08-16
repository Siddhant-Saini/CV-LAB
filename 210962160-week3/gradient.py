import cv2
import numpy as np

# Load the image
image_path = './resource/nature.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Compute gradients using Sobel operators
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Compute magnitude and angle of gradients
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_angle = np.arctan2(gradient_y, gradient_x) * (180 / np.pi)

# Display the gradient magnitude and angle images
cv2.imshow('Gradient Magnitude', gradient_magnitude.astype(np.uint8))
cv2.imshow('Gradient Angle', gradient_angle.astype(np.uint8))

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
