import cv2
import numpy as np

# Load the image
image_path = './resource/nature.jpeg'
image = cv2.imread(image_path)

if image is None:
    print("Image not found.")
else:
    # Apply box filter
    box_filtered = cv2.boxFilter(image, -1, (5, 5))

    # Apply Gaussian fqilter
    gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the original, box-filtered, and Gaussian-filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Box Filtered Image', box_filtered)
    cv2.imshow('Gaussian Filtered Image', gaussian_filtered)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
