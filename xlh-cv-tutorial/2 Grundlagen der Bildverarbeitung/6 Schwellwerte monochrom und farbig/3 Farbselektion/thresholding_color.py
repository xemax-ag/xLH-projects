# thresholding_color.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0
WHITE_3 = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')
# Gaussian Blurfilter
blurred = cv2.GaussianBlur(image, (9, 9), 0)

# transformiere das Bild in den HSV Bereich
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# (h_min, s_min, v_min)
# (h_max, s_max, v_max)
threshold_color = cv2.inRange(image_hsv,
                              (15, 100,  50),
                              (45, 255, 255))

# Morphologische Operationen
eroded = cv2.erode(threshold_color, None, iterations=2)
dilate = cv2.dilate(eroded, None, iterations=2)

# Maskierung vom Ursprungsbild mit dem Schwellwertbild
masked = cv2.bitwise_and(image, image, mask=dilate)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
image_hsv = cv2.putText(image_hsv, 'Original HSV', (25, 25),
                        font, 0.8, WHITE, 2, cv2.LINE_AA)
masked = cv2.putText(masked, 'Maskierung', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)

threshold_color = cv2.putText(threshold_color, 'Schwellwert', (25, 25),
                              font, 0.8, WHITE, 2, cv2.LINE_AA)
eroded = cv2.putText(eroded, 'Erodierung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
dilate = cv2.putText(dilate, 'Erweiterung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
result_1 = np.hstack([threshold_color, eroded, dilate])
result_2 = np.hstack([image, image_hsv, masked])

# schreibe das Bild in eine Datei
cv2.imwrite('img/thresholding_color_1.png', result_1[0:-2, 0:-2])
cv2.imwrite('img/thresholding_color_2.png', result_2[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe 1', result_1)
cv2.imshow('Ausgabe 2', result_2)
cv2.moveWindow('Ausgabe 1', 100, 100)
cv2.moveWindow('Ausgabe 2', 100, 500)
cv2.waitKey(0)
