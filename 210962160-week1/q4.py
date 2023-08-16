import cv2

# Load the image
image_path = './resource/mountains.jpg'
image = cv2.imread(image_path)

# Specify the rectangle's top-left and bottom-right coordinates
top_left = (100, 50)
bottom_right = (300, 200)

# Draw the rectangle on the image
color = (0, 255, 0)  # Green color in BGR format
thickness = 2       # Thickness of the rectangle's border
cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Display the image with the drawn rectangle
cv2.imshow('Image with Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
