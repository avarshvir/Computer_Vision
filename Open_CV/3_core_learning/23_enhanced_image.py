import cv2

img = cv2.imread('../resources/images/img3.jpg')

# Step 1: Brightness & contrast
enhanced = cv2.convertScaleAbs(img, alpha=1.4, beta=40)

# Step 2: CLAHE on grayscale version
gray = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_result = clahe.apply(gray)

# Display
cv2.imshow('Original', img)
cv2.imshow('Contrast + Brightness Enhanced', enhanced)
cv2.imshow('CLAHE (Grayscale)', clahe_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
