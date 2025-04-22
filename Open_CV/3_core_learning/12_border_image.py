# Python program to explain cv2.copyMakeBorder() method 

# importing cv2 
import cv2 

# path 
path = '../resources/images/img2.jpg'

# Reading an image in default mode 
image = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

# Using cv2.copyMakeBorder() method 
#image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = 0) 
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = (255,0,0)) 
#image = cv2.copyMakeBorder(image, 100, 100, 50, 50, cv2.BORDER_REFLECT) 


# Displaying the image 
cv2.imshow(window_name, image) 

cv2.waitKey(0)
cv2.destroyAllWindows()
