import cv2

# Load the image
image_path = './resource/mountains.jpg'
image = cv2.imread(image_path)

# Define the new dimensions for resizing
new_width = 800
new_height = 600

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Display the original and resized images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
