# template_ipcam.py
import cv2
import numpy as np
from fps import Fps

# capture video stream from webcam
# cap = cv2.VideoCapture(camera_nr, cv2.CAP_DSHOW)
# https://stackoverflow.com/questions/20891936/rtsp-stream-and-opencv-python
# https://stackoverflow.com/questions/60816436/open-cv-rtsp-camera-buffer-lag
# https://discuss.mxnet.apache.org/t/object-detection-reading-from-rtsp-stream-with-no-buffer/6591

cap = cv2.VideoCapture('rtsp://192.168.1.21:8554/cam')
# cap = cv2.VideoCapture('rtsp://192.168.31.31:8554/cam')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

fps = Fps()

while True:
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame_rotated = cv2.rotate(frame_bgr, cv2.ROTATE_180)
        fps.update()
        if ret:
            cv2.imshow('frame', frame_rotated)
            #cv2.moveWindow('frame', 0, 0)
    else:
        print('not opened')

    cv2_key = cv2.waitKey(1) & 0xFF
    if cv2_key == ord('q'):
        break
    elif cv2_key == ord('s'):
        print('save frame as png')
        cv2.imwrite("frame.png", frame)
    elif cv2_key == ord('f'):
        print(f'fps: {fps.fps:1.1f}')
    elif cv2_key == ord('r'):
        print(np.shape(frame))

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
