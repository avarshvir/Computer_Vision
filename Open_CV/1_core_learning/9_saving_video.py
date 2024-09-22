import cv2

cap = cv2.VideoCapture('../resources/videos/video1.mp4')

if(cap.isOpened() == False):
    print("Error")

# writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter("../resources/videos/video2.avi",cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        out.write(frame)
        cv2.imshow("Video2",frame)
        if(cv2.waitKey(5) & 0xFF == ord('q')):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()