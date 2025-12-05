# green_screen_step_3.py
import cv2
import imutils
import numpy as np
from fps import Fps

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0
BLACK_3 = (0, 0, 0)
WHITE_3 = (255, 255, 255)

# capture video stream from file
cap = cv2.VideoCapture('../../5 Videos/green_screen.mp4')

cap_nr_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap_fps = cap.get(cv2.CAP_PROP_FPS)
# cap_fps = 1

cap_time = cap_nr_of_frames / cap_fps
print(cap_width, cap_height, cap_nr_of_frames, cap_fps, cap_time)
fps = Fps(estimaeted_fps=cap_fps)

# lade Hintergrundbild von der Datei in ein NumPy Array
background = cv2.imread('img/background.png')
background = imutils.resize(background, width=480)

while (True):
    if cap.isOpened():
        # capture
        ret, image = cap.read()
        if ret:
            image = imutils.resize(image, width=480)
            fps.delay()

            # Gaussian Blurfilter
            blurred = cv2.GaussianBlur(image, (9, 9), 0)

            # transformiere das Bild in den HSV Bereich
            image_hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            # Schwellwertbetrachtung
            threshold_color = cv2.inRange(image_hsv, (40, 0, 0), (70, 255, 255))

            # Erodierung, Dilate
            eroded = cv2.erode(threshold_color, None, iterations=2)
            dilated = cv2.dilate(eroded, None, iterations=2)
            dilated_not = cv2.bitwise_not(dilated)

            # Die Maske muss in der gleichen Farbdimension des Bildes liegen.
            masked_image = cv2.bitwise_and(image, image, mask=dilated)
            masked_image_invers = cv2.bitwise_and(image, image, mask=dilated_not)
            masked_background = cv2.bitwise_and(background, background, mask=dilated)

            # Addition der Maskierungen
            new_image = cv2.add(masked_background, masked_image_invers)

            # Zusammenfassung der Ausganslage und der Bearbeitung
            image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
            masked_image = cv2.putText(masked_image, 'Maskierung', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
            masked_image_invers = cv2.putText(masked_image_invers, 'Maskierung invers', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
            threshold_color = cv2.putText(threshold_color, 'Schwellwert', (25, 25),
                                          font, 0.8, BLACK, 2, cv2.LINE_AA)
            masked_background = cv2.putText(masked_background, 'Maskierung Hintergrund', (25, 25),
                                            font, 0.8, WHITE_3, 2, cv2.LINE_AA)
            new_image = cv2.putText(new_image, 'neues Bild', (25, 25),
                                    font, 0.8, WHITE_3, 2, cv2.LINE_AA)

            eroded = cv2.putText(eroded, 'Erodierung', (25, 25), font, 0.8, BLACK, 2, cv2.LINE_AA)
            dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, BLACK, 2, cv2.LINE_AA)
            result_1 = np.hstack([threshold_color, eroded, dilated])
            result_2 = np.hstack([image, masked_image, masked_image_invers])
            result_3 = np.hstack([masked_image_invers, masked_background, new_image])

            # Anzeige auf dem Bildschirm
            cv2.imshow('Ausgabe 1', result_1)
            cv2.imshow('Ausgabe 2', result_2)
            cv2.imshow('Ausgabe 3', result_3)
            cv2.moveWindow('Ausgabe 1', 100, 100)
            cv2.moveWindow('Ausgabe 2', 100, 425)
            cv2.moveWindow('Ausgabe 3', 100, 750)

        else:
            print('break')
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
