import cv2

img = cv2.imread('../resources/images/img3.jpg')

g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray image',g_img)

cv2.waitKey(0)
cv2.destroyAllWindows()