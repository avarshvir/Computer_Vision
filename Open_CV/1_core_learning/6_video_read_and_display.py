import cv2

cap = cv2.VideoCapture("../resources/videos/video1.mp4")

if(cap.isOpened() == False):
    print("Error in playing video.")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("Video 1", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()