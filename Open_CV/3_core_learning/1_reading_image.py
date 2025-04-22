import cv2

img = cv2.imread('../resources/images/image2000.png', flags=0)
cv2.imshow("image", img)
cv2.waitKey(0)                     #we can change 0 to other numbers also for seconds such as 5000 == 5 sec.
cv2.destroyAllWindows()