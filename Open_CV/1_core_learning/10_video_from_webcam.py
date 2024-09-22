import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    if(ret == True):
        cv2.imshow("Webcam_Video",frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()