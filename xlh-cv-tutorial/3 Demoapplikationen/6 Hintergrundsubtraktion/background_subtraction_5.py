# background_subtraction_5.py
import cv2
import imutils
import numpy as np

from background_subtraction_4 import BackgroundSubtraction
from fps import Fps

# öffne Videostream
cap = cv2.VideoCapture('../../5 Videos/background_subtraction.mp4')
# Erfassung der Videoeigenschaften
cap_nr_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_fps = cap.get(cv2.CAP_PROP_FPS)
cap_fps = 5  # frames per second
cap_time = cap_nr_of_frames / cap_fps
print(cap_width, cap_height, cap_nr_of_frames, cap_fps, cap_time)
fps = Fps(estimaeted_fps=cap_fps)

# Instanzierungq
back_sub_inst = BackgroundSubtraction()

while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        if ret:
            # erfasse Einzelbild aus dem Videostream
            frame = imutils.resize(frame, width=480)
            fps.delay()

            center_of_mass = back_sub_inst.apply_sub(frame)

            result = np.hstack([frame, center_of_mass])

            # Anzeige auf dem Bildschirm
            cv2.imshow('Ausgabe', result)
            cv2.moveWindow('Ausgabe', 100, 100)
        else:
            break
    else:
        # Filmende
        break

    cv2_key = cv2.waitKey(1) & 0xFF
    if cv2_key == ord('q'):
        break
    elif cv2_key == ord('s'):
        print('save frame as png')
        cv2.imwrite("img/frame.png", frame)
    elif cv2_key == ord('f'):
        print(f'fps: {fps.fps:1.1f}')

# Freigabe des Videostreams
cap.release()
cv2.destroyAllWindows()
