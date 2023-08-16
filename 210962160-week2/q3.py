import cv2

# Load the image
image_path = './resource/nature.jpeg'
image = cv2.imread(image_path)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Resize the image
new_width = 300
new_height = 200
resized_image = cv2.resize(image, (new_width, new_height))

# Display the resized image
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)

# Define the coordinates for cropping
start_x, start_y = 50, 30
end_x, end_y = 250, 170

# Crop the image
cropped_image = image[start_y:end_y, start_x:end_x]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
