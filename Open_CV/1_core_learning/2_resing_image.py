# Resizing Image
import cv2
img = cv2.imread("../resources/images/img4.jpg")
img1 = cv2.resize(img,(1200,680))

#cv2.imshow("Image Original", img)
cv2.imshow("Image Resize", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()