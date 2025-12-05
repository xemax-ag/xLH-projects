# YOLO V8: https://pypi.org/project/ultralytics/ , pip install ultralytics 8.1.2
# https://docs.ultralytics.com/modes/track/#tracker-selection
# https://docs.ultralytics.com/modes/predict/#introduction

import cv2
from ultralytics import YOLO

# ToDo: Package requirements: Ultralytics requirement ['lapx>=0.5.2'] not found, attempting AutoUpdate
# ['lapx>=0.5.2']


# Load the YOLOv8 model
# https://docs.ultralytics.com/tasks/detect/
# model = YOLO('yolov8n.pt')  # Load an official Detect model
# model = YOLO('yolov8x.pt')  # Load an official Detect model
# model = YOLO('yolov8n-seg.pt')  # Load an official Segment model
# model = YOLO('yolov8x-seg.pt')  # Load an official Segment model
model = YOLO('yolov8n-pose.pt')  # Load an official Pose model
# model = YOLO('yolov8x-obb.pt')  # Load an official Pose model

# Open the video file
# video_path = "path/to/video.mp4"
# cap = cv2.VideoCapture(video_path)

camera_nr = 0   # 0 = default, 1,2,3 = extra webcam
cap = cv2.VideoCapture(camera_nr, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)
        # results = model(frame)  # obb

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()