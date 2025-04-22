import cv2

# path 
path = '../resources/images/img2.jpg'

# Reading an image in default mode 
image = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

image = cv2.copyMakeBorder(image, 100, 100, 70, 70, cv2.BORDER_REFLECT)

cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()