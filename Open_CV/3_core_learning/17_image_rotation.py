"""
img.shape[:2] extracts the height (h) and width (w) of the image.
center calculates the center point of the image around which the rotation will occur.
---------------------------------------------------------------------
cv2.getRotationMatrix2D(center, angle, scale) Explained:
center: Tuple (x, y) — point around which rotation happens.
angle: Angle in degrees, positive values mean counter-clockwise rotation.
scale: Zoom factor during rotation.
1.0 → keeps size unchanged
>1.0 → zooms in
<1.0 → zooms out
-----------------------------------------------------------------------
cv2.warpAffine(image, M, dsize) Explained:
image: The original image.
M: The transformation matrix (from getRotationMatrix2D).
dsize: The output image size — here it's (w, h) (same size as input).

"""

import cv2

img_path = '../resources/images/image2000.png'

img = cv2.imread(img_path)

#get image dimensions

(h,w) = img.shape[:2]
center = (w//2,h//2)

# Define rotation matrix (e.g., 45 degrees, scale = 1.0)
angle = 60
scale = 0.5

M = cv2.getRotationMatrix2D(center, angle, scale)

# Perform the rotation
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow('rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()