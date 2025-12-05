# template_ipcam.py
import cv2
import numpy as np
from fps import Fps

# capture video stream from webcam
camera_nr = 2   # 0 = default, 1,2,3 = extra webcam
cap = cv2.VideoCapture(camera_nr, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

fps = Fps()

while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        fps.update()
        if ret:
            cv2.imshow('frame', frame)
            #cv2.moveWindow('frame', 0, 0)

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
