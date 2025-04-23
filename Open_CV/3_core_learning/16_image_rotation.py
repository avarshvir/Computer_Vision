import cv2

img_path = '../resources/images/image2000.png'

or_img = cv2.imread(img_path)

rot_90_c = cv2.rotate(or_img, cv2.ROTATE_90_CLOCKWISE)

rot_180 = cv2.rotate(or_img, cv2.ROTATE_180)

rot_90_cc = cv2.rotate(or_img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('Original Image', or_img)

cv2.imshow('90 rotate', rot_90_c)

cv2.imshow('90 rotate cc', rot_90_cc)

cv2.imshow('180 rotate', rot_180)

cv2.waitKey(0)

cv2.destroyAllWindows()
