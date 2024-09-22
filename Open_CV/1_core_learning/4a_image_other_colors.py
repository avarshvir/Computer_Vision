import cv2
img = cv2.imread('../resources/images/img4.jpg')
color_change = cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
cv2.imshow('Image1',color_change)
cv2.waitKey(0)
cv2.destroyAllWindows()