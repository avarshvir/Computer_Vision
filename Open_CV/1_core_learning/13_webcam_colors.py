import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    color_change = cv2.cvtColor(frame,cv2.COLOR_BGR2LUV)
    if(ret == True):
        cv2.imshow("Colored_Webcam",color_change)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()