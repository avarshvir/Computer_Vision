import cv2

# Load the image
img = cv2.imread('../resources/images/img3.jpg')

# Increase contrast (alpha > 1) and brightness (beta > 0)
alpha = 1.5  # Contrast control (1.0–3.0)
beta = 30    # Brightness control (0–100)

# Enhance the image
enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Display
cv2.imshow('Original', img)
cv2.imshow('Enhanced (Contrast + Brightness)', enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
