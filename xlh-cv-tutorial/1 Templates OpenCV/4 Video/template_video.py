# videostream_from_mp4.py
import cv2
from fps import Fps

# capture video stream from file
cap = cv2.VideoCapture('../../5 Videos/cats.mp4')

cap_nr_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_fps = cap.get(cv2.CAP_PROP_FPS)
cap_time = cap_nr_of_frames / cap_fps
print(cap_width, cap_height, cap_nr_of_frames, cap_fps, cap_time)
fps = Fps(estimaeted_fps=cap_fps)

while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        fps.delay()
        if ret:
            cv2.imshow('frame', frame)
            cv2.moveWindow('frame', 0, 0)
        else:
            break

    cv2_key = cv2.waitKey(1) & 0xFF
    if cv2_key == ord('q'):
        break
    elif cv2_key == ord('s'):
        print('save frame as png')
        cv2.imwrite("frame.png", frame)
    elif cv2_key == ord('f'):
        print(f'fps: {fps.fps:1.1f}')

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
