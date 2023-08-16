import cv2
import numpy as np

# Load the image
image_path = './resource/nature.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply the log transformation
c = 255 / np.log(1 + np.max(image))
log_transformed_image = c * np.log(image + 1)

# Convert the float values back to uint8 range
log_transformed_image = np.uint8(log_transformed_image)

# Display the original and log-transformed images
cv2.imshow('Original Image', image)
cv2.imshow('Log-Transformed Image', log_transformed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
