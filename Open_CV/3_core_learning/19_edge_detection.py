import cv2
import numpy as np

# Load image in grayscale
img = cv2.imread('../resources/images/image2000.png', cv2.IMREAD_GRAYSCALE)

# Apply Sobel operator to find horizontal and vertical edges

# Sobel kernel for horizontal edges (Gx)
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel kernel for vertical edges (Gy)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradient (edge strength)
magnitude = cv2.magnitude(sobel_x, sobel_y)

# Convert the result to 8-bit (for display)
magnitude = np.uint8(np.absolute(magnitude))

# Show the results
cv2.imshow('Original Image', img)
cv2.imshow('Sobel X (Horizontal Edges)', sobel_x)
cv2.imshow('Sobel Y (Vertical Edges)', sobel_y)
cv2.imshow('Gradient Magnitude (Edges)', magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()
