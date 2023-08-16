import cv2

# Path to the video file
video_path = './resource/cv_video.mp4'

# Open the video file
video_capture = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not video_capture.isOpened():
    print("Error opening video file")
    exit()

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
