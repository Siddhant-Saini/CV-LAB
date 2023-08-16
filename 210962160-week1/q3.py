import cv2

# Load the image
image_path = './resource/mountains.jpg'
image = cv2.imread(image_path)

# Choose the pixel coordinates (row, column) you want to extract RGB values from
pixel_row = 100
pixel_col = 150

# Extract the RGB values of the chosen pixel
blue_value = image[pixel_row, pixel_col, 0]
green_value = image[pixel_row, pixel_col, 1]
red_value = image[pixel_row, pixel_col, 2]

# Print the RGB values
print(f"RGB values of pixel ({pixel_row}, {pixel_col}):")
print(f"Red: {red_value}")
print(f"Green: {green_value}")
print(f"Blue: {blue_value}")
