import cv2

# Open the video file
cap = cv2.VideoCapture('../resources/videos/video1.mp4')

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the width and height of the video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)  # Get the frames per second

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
out = cv2.VideoWriter('../resources/videos/output_video.avi', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Write the frame to the output video
        out.write(frame)

        # Display the frame
        cv2.imshow("Video2", frame)

        # Exit on 'q' key press
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything
cap.release()
out.release()  # Release the VideoWriter object
cv2.destroyAllWindows()
