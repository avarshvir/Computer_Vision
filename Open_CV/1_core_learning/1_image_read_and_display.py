# Reading an image and displaying it
import cv2
img = cv2.imread("../resources/images/img4.jpg")
cv2.imshow("image 1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()