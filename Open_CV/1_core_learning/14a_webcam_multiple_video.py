import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Convert to grayscale
        gray_cap = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale to black and white (binary)
        (thresh, b_w) = cv2.threshold(gray_cap, 127, 255, cv2.THRESH_BINARY)

        # Apply a colormap to the grayscale image for color representation
        gray_color = cv2.applyColorMap(gray_cap, cv2.COLORMAP_JET)

        # Convert binary (black and white) to a 3-channel image
        b_w_color = cv2.cvtColor(b_w, cv2.COLOR_GRAY2BGR)

        # Display the original, grayscale, black and white, and colored conversions
        cv2.imshow("Original", frame)
        cv2.imshow("Gray", gray_cap)
        cv2.imshow("Black and White", b_w)
        cv2.imshow("Grayscale to Color", gray_color)  # Apply colormap
        cv2.imshow("Black and White to Color", b_w_color)  # Black and white remains BGR

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
