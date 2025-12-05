# green_screen_step_2.py
import cv2
import numpy as np
import imutils
from fps import Fps

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0
WHITE_3 = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# erfasse den Videostream
cap = cv2.VideoCapture('../../5 Videos/object_tracking.mp4')
cap_nr_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_fps = cap.get(cv2.CAP_PROP_FPS)
# cap_fps = 5
cap_time = cap_nr_of_frames / cap_fps
print(cap_width, cap_height, cap_nr_of_frames, cap_fps, cap_time)
fps = Fps(estimaeted_fps=cap_fps)

while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        fps.delay()
        if ret:
            frame = imutils.resize(frame, width=480)

            # Gaussian Blurfilter
            blurred = cv2.GaussianBlur(frame, (9, 9), 0)

            # transformiere das Bild in den HSV Bereich
            image_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Schwellwertbetrachtung
            threshold_color = cv2.inRange(image_hsv, (20, 0, 0), (50, 255, 255))

            # Erodierung, Dilate
            eroded = cv2.erode(threshold_color, None, iterations=5)
            dilated = cv2.dilate(eroded, None, iterations=5)
            dilated_not = cv2.bitwise_not(dilated)

            # finde alle äusseren Konturen und markiere diese im Bild
            cnts, hir = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            conturs = frame.copy()
            cv2.drawContours(conturs, cnts, -1, GREEN, 2)

            # loop über die einzelnen Konturen
            min_circle = frame.copy()
            for (i, c) in enumerate(cnts):
                # berechne
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                # print(x, y, radius)
                if radius > 18:
                    # zeichne den Kreis
                    cv2.circle(min_circle, (int(x), int(y)), 5, RED, -1)
                    cv2.circle(min_circle, (int(x), int(y)), int(radius), RED, 2)
                    min_circle = cv2.putText(min_circle, f'{int(x)} / {int(y)}', ((int(x) + 35), (int(y) + 5)),
                                             font, 0.5, RED, 1, cv2.LINE_AA)

            # Zusammenfassung der Ausganslage und der Bearbeitung
            frame = cv2.putText(frame, 'Original', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
            conturs = cv2.putText(conturs, 'Konturen', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
            min_circle = cv2.putText(min_circle, 'Ballerkennung', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)

            threshold_color = cv2.putText(threshold_color, 'Schwellwert', (25, 25),
                                          font, 0.8, WHITE, 2, cv2.LINE_AA)
            eroded = cv2.putText(eroded, 'Erodierung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
            dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
            result_1 = np.hstack([threshold_color, eroded, dilated])
            result_2 = np.hstack([frame, conturs, min_circle])

            # Anzeige auf dem Bildschirm
            cv2.imshow('Ausgabe 1', result_1)
            cv2.imshow('Ausgabe 2', result_2)
            cv2.moveWindow('Ausgabe 1', 100, 100)
            cv2.moveWindow('Ausgabe 2', 100, 400)
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
