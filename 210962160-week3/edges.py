import cv2

# Load the image
image_path = './resource/nature.jpeg'
original_image = cv2.imread(image_path)

if original_image is None:
    print("Image not found.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

    # Display the original image and the detected edges
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Detected Edges (Canny)', edges)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
