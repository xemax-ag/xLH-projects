# green_screen_step_5.py
import cv2
import imutils

from fps import Fps
from green_screen_step_4 import GreenScreen

if __name__ == '__main__':
    # Instanzierung der Klasse
    green_screen = GreenScreen()

    # capture video stream from file
    cap = cv2.VideoCapture('../../../Videos/Videos/video/green_screen.mp4')

    # lade Hintergrundbild von der Datei in ein NumPy Array
    background = cv2.imread('img/background.png')
    background = imutils.resize(background, width=960)

    cap_nr_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap_fps = cap.get(cv2.CAP_PROP_FPS)
    cap_time = cap_nr_of_frames / cap_fps
    print(cap_width, cap_height, cap_nr_of_frames, cap_fps, cap_time)
    fps = Fps(estimaeted_fps=cap_fps)

    while (True):
        if cap.isOpened():
            # capture
            ret, frame = cap.read()
            if ret:
                frame = imutils.resize(frame, width=960)
                fps.delay()
                new_image = green_screen.replace_green_screen(frame.copy(), background)
                cv2.imshow('frame', new_image)
                cv2.moveWindow('frame', 100, 100)
            else:
                break

        cv2_key = cv2.waitKey(1) & 0xFF
        if cv2_key == ord('q'):
            break
        elif cv2_key == ord('s'):
            print('save frame as png')
            cv2.imwrite("green_screen_background.png", new_image)
        elif cv2_key == ord('f'):
            print(f'fps: {fps.fps:1.1f}')

    # when everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
