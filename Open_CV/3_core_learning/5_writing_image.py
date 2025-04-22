import cv2

img = cv2.imread('../resources/images/img3.jpg', flags = 1)

cv2.imshow('anime dusk', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
try:
    cv2.imwrite("../resources/newly_write/anime_dusk.jpg",img)
    print("image is saved")
except Exception as e:
    print(f"Image is already save {e}")
