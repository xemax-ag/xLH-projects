# green_screen_step_2.py
import cv2
import numpy as np
import imutils

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0
WHITE_3 = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/frame.png')
image = imutils.resize(image, width=480)

# Gaussian Blurfilter
blurred = cv2.GaussianBlur(image, (9, 9), 0)

# transformiere das Bild in den HSV Bereich
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Schwellwertbetrachtung
threshold_color = cv2.inRange(image_hsv, (20, 0, 0), (50, 255, 255))

# Erodierung, Dilate
eroded = cv2.erode(threshold_color, None, iterations=2)
dilated = cv2.dilate(eroded, None, iterations=2)
dilated_not = cv2.bitwise_not(dilated)

# finde alle äusseren Konturen und markiere diese im Bild
cnts, hir = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conturs = image.copy()
cv2.drawContours(conturs, cnts, -1, GREEN, 2)

# loop über die einzelnen Konturen
min_circle = image.copy()
for (i, c) in enumerate(cnts):
    # berechne
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    print(x, y, radius)
    if radius > 15:
        # zeichne den Kreis
        cv2.circle(min_circle, (int(x), int(y)), 5, RED, -1)
        cv2.circle(min_circle, (int(x), int(y)), int(radius), RED, 2)
        min_circle = cv2.putText(min_circle, f'{int(x)} / {int(y)}', ((int(x)+35), (int(y)+5)),
                                 font, 0.5, RED, 1, cv2.LINE_AA)


# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
conturs = cv2.putText(conturs, 'Konturen', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
min_circle = cv2.putText(min_circle, 'Ballerkennung', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
threshold_color = cv2.putText(threshold_color, 'Schwellwert', (25, 25),
                              font, 0.8, WHITE, 2, cv2.LINE_AA)
eroded = cv2.putText(eroded, 'Erodierung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
result_1 = np.hstack([threshold_color, eroded, dilated])
result_2 = np.hstack([image, conturs, min_circle])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe 1', result_1)
cv2.imshow('Ausgabe 2', result_2)
cv2.moveWindow('Ausgabe 1', 100, 100)
cv2.moveWindow('Ausgabe 2', 100, 400)
cv2.waitKey(0)
