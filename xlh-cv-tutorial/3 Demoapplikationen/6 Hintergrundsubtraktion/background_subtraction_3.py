# background_subtraction_3.py
import cv2
from fps import Fps
import imutils
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)

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

# Hintergrundsubtraktion
back_sub = cv2.createBackgroundSubtractorMOG2()
back_sub.setDetectShadows(True)
back_sub.setShadowValue(0)
back_sub.setHistory(1000)

while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        if ret:
            # erfasse Einzelbild aus dem Videostream
            frame = imutils.resize(frame, width=480)
            fps.delay()

            # Maskierung der Bilddifferenz
            fgMask = back_sub.apply(frame, learningRate=0.01)

            # entferne Pixelrauschenq
            eroded = cv2.erode(fgMask, None, iterations=2)

            # verbinden von weissen Einzelpunkten
            dilated = cv2.dilate(eroded, None, iterations=20)

            # Maskierung der bewegten Bildelement aus dem Ursprungsframe
            masked = cv2.bitwise_and(frame, frame, mask=dilated)

            # finde alle äusseren Konturen und markiere diese im Bild
            masked_gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
            cnts, hir = cv2.findContours(masked_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            conturs = frame.copy()
            cv2.drawContours(conturs, cnts, -1, GREEN, 2)

            # loop over the contours again
            center_of_mass = masked.copy()
            for (i, c) in enumerate(cnts):
                # compute the area and the perimeter of the contour
                area = cv2.contourArea(c)
                perimeter = cv2.arcLength(c, True)
                # print('Contour #{} -- area: {:.2f}, perimeter: {:.2f}'.format(i + 1, area, perimeter))
                if area > 3000:
                    # draw the contour on the image
                    cv2.drawContours(center_of_mass, [c], -1, GREEN, 2)
                    # compute the center of the contour and draw the contour number
                    M = cv2.moments(c)
                    cX = int(M['m10'] / M['m00'])
                    cY = int(M['m01'] / M['m00'])
                    cv2.circle(center_of_mass, (cX, cY), 5, RED, -1)

            result_1 = np.hstack([fgMask, eroded, dilated])
            result_2 = np.hstack([frame, masked])
            result_3 = np.hstack([conturs, center_of_mass])

            # Anzeige auf dem Bildschirm
            cv2.imshow('Ausgabe 1', result_1)
            cv2.imshow('Ausgabe 2', result_2)
            cv2.imshow('Ausgabe 3', result_3)
            cv2.moveWindow('Ausgabe 1', 100, 100)
            cv2.moveWindow('Ausgabe 2', 100, 400)
            cv2.moveWindow('Ausgabe 3', 100, 700)
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
