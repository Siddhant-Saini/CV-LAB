import numpy as np
import cv2

image_path = './resource/nature.jpeg'
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 2.5)

unsharp_mask = cv2.subtract(gray_image, blurred_image)

sharpened_image = cv2.add(gray_image, unsharp_mask)

stacked_images = np.hstack((image, cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), cv2.cvtColor(sharpened_image, cv2.COLOR_GRAY2BGR)))

cv2.imshow('Image Comparison (Original - Grayscale - Sharpened)', stacked_images)
cv2.waitKey(0)
cv2.destroyAllWindows()
