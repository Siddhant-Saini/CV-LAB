import cv2
import numpy as np

# Load the image
image_path = './resource/nature.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5),1.4)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

# Show the original image and the edges side by side
stacked_images = np.hstack((image, edges))
cv2.imshow('Original Image vs. Edges', stacked_images)
cv2.waitKey(0)
cv2.destroyAllWindows()
