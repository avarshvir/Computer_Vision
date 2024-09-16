# saving or writing an image
import cv2
img = cv2.imread("../resources/images/img7.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


(thresh, b_w) = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)

cv2.imwrite("../resources/newly_write/Black_White_Image.png",b_w)

'''
cv2.imshow("Color image", img)
cv2.imshow("Gray Image",gray_img)
cv2.imshow("Black and White Image", b_w)
cv2.waitKey(0)
cv2.destroyAllWindows()'''