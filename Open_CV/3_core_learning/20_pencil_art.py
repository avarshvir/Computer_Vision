import cv2
import numpy as np

img = cv2.imread('../resources/images/img3.jpg', cv2.IMREAD_GRAYSCALE)

# Invert image
inv_img = 255 - img

# Blur inverted image
blur_img = cv2.GaussianBlur(inv_img, (21, 21), 0)

# Invert the blur
inv_blur = 255 - blur_img

# Blend original with inverted blur (this is the sketch effect!)
sketch = cv2.divide(img, inv_blur, scale=256.0)

cv2.imshow("Pencil Sketch", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
