import cv2

img_path = '../resources/images/image2000.png'

original_image = cv2.imread(img_path)

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

_,bw = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

edge_image = cv2.Canny(gray_image, 100,200)

cv2.imshow('original image', original_image)
cv2.imshow('gray image', gray_image)
cv2.imshow('bw image', bw)
cv2.imshow('edge image', edge_image)

cv2.waitKey(0)
cv2.destroyAllWindows()