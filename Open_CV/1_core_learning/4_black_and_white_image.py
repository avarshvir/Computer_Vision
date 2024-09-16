# Black and White Image
import cv2
img = cv2.imread("../resources/images/img8.jpg")
img2 = cv2.resize(img,(300,300))
gray_img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

(thresh, b_w) = cv2.threshold(gray_img,127,255, cv2.THRESH_BINARY)

cv2.imshow("color img", img2)
cv2.imshow("gray img", gray_img)
cv2.imshow("black_and_white img", b_w)

cv2.waitKey(0)
cv2.destroyAllWindows()