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