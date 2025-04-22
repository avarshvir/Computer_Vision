import cv2
import matplotlib.pyplot as plt
img = cv2.imread('../resources/images/image2000.png')

plt.imshow(img)
plt.waitforbuttonpress()
plt.close('all')