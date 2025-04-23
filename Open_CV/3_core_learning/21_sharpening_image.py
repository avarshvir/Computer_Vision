import cv2
import numpy as np

img = cv2.imread('../resources/images/img3.jpg')

# Define sharpening kernel
kernel = np.array([[ 0, -1,  0],
                   [-1,  5, -1],
                   [ 0, -1,  0]])

# Apply sharpening
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
