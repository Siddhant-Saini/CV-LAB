import cv2

# Load the image
image_path = './resource/mountains.jpg'
image = cv2.imread(image_path)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Write the grayscale image to disk
output_path = './resource/output_gray_image.jpg'
cv2.imwrite(output_path, gray_image)

# Load and display the written image
written_image = cv2.imread(output_path)
cv2.imshow('Written Grayscale Image', written_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
