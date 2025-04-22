"""
Other Borders
cv2.BORDER_REPLICATE     # Repeat edge pixels
cv2.BORDER_REFLECT       # Mirror the border (with edge pixel repeated)
cv2.BORDER_REFLECT_101   # Mirror without repeating the edge pixel
cv2.BORDER_WRAP          # Wrap around the image
"""


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