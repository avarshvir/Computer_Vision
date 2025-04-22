import cv2

img1 = cv2.imread('../resources/images/image2000.png')

res_img = cv2.resize(img1, (1600, 800))
cv2.imshow('resized_image',res_img)
print(img1.shape)
print(res_img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()