# color to grey image
import cv2
img = cv2.imread("../resources/images/img4.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Color Image", img)
cv2.imshow("Gray Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()