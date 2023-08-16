import cv2

# Load the image
image_path = './resource/mountains.jpg'
image = cv2.imread(image_path)

# Define the rotation angle in degrees
rotation_angle = 45

# Get the dimensions of the image
height, width = image.shape[:2]

# Calculate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), rotation_angle, 1)

# Apply the rotation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
