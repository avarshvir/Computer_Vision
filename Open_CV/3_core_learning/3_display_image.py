import cv2

path = '../resources/images/img2.jpg'
win_name = 'Anime Scence'

img = cv2.imread(path, flags=1)
cv2.imshow(win_name,img)
cv2.waitKey(0)
cv2.destroyAllWindows()