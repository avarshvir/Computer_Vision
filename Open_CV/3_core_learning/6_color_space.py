import cv2

img = cv2.imread('../resources/images/img8.jpg')

B, G, R = cv2.split(img)

cv2.imshow('Original Image', img)
cv2.waitKey(0)

cv2.imshow('Blue',B)
cv2.waitKey(0)

cv2.imshow('Green', G)
cv2.waitKey(0)

cv2.imshow('Red', R)
cv2.waitKey(0)

cv2.destroyAllWindows()