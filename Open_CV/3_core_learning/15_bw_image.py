import cv2

img = cv2.imread('../resources/images/img3.jpg')

g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, bw = cv2.threshold(g_img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('original', img)
cv2.imshow('Gray', g_img)
cv2.imshow('B_W', bw)

cv2.waitKey(0)
cv2.destroyAllWindows()