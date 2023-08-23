import cv2 as cv
import numpy as np

# Load an image
image = cv.imread('./resources/sudoku.jfif')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply edge detection (Canny) to the image
edges = cv.Canny(gray, 50, 150, apertureSize=3)

# Apply Hough Line Transform
lines = cv.HoughLines(edges, 1, np.pi / 180, threshold=150)

# Draw the detected lines on the original image
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the original image with detected lines
cv.imshow('Detected edges', edges)
cv.imshow('Detected Lines', image)

cv.waitKey(0)
cv.destroyAllWindows()
