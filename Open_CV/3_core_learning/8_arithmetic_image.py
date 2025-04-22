import cv2

img1 = cv2.imread('../resources/images/img2.jpg')
img2 = cv2.imread('../resources/images/img6.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

sub = cv2.subtract(img1,img2)

cv2.imshow('subtracted',sub)

cv2.waitKey(0)
cv2.destroyAllWindows()