import cv2

cap = cv2.VideoCapture("../resources/videos/video1.mp4")
#cap = cv2.VideoCapture(0)

if(cap.isOpened() == False):
    print("Error in playing video.")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video 1", gray_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()