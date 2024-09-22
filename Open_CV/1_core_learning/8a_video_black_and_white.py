import cv2
cap = cv2.VideoCapture("../resources/videos/video1.mp4")

if (cap.isOpened() == False):
    print("Error")

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        gray_vid = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        (thresh,b_w) = cv2.threshold(gray_vid,127,255,cv2.THRESH_BINARY)
        cv2.imshow("vid1",b_w)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()