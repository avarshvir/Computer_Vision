import cv2
cap = cv2.VideoCapture('../resources/videos/video1.mp4')

if (cap.isOpened() == False):
    print("Error.....")

while(True):
    (ret, frame) = cap.read()

    if not ret:
        break

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, b_w) = cv2.threshold(grayframe, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Black and White Video', b_w)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()