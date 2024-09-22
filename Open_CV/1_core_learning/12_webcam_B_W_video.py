import cv2

cap = cv2.VideoCapture(0)


while(cap.isOpened()):
    ret,frame = cap.read()
    gray_cap = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, b_w) = cv2.threshold(gray_cap,127,255,cv2.THRESH_BINARY)
    if(ret == True):
        cv2.imshow("Black and White",b_w)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()