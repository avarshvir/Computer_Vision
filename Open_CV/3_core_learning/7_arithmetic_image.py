import cv2
import numpy as np

#img1_path = '../resources/images/img2.jpg'
#img2_path = '../resources/images/img6.jpg'

img1 = cv2.imread('../resources/images/img2.jpg')
img2 = cv2.imread('../resources/images/img1.jpg')

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


#print(img1.shape)
#print(img2.shape)


weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)

# with the weighted sum  
cv2.imshow('Weighted Image', weightedSum) 
  
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
   cv2.destroyAllWindows() 

cv2.imwrite('../resources/newly_write/add_img.jpg',weightedSum)


