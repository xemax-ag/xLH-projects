# green_screen_step_3.py
import cv2
import imutils
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
BLACK_3 = (0, 0, 0)
WHITE_3 = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/green_screen.png')
image = imutils.resize(image, width=480)

# lade Hintergrundbild von der Datei in ein NumPy Array
background = cv2.imread('img/background.png')
background = imutils.resize(background, width=480)

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
masked_image_invers = cv2.bitwise_and(image, image, mask=dilated_not)
masked_background = cv2.bitwise_and(background, background, mask=dilated)

# Addition der Maskierungen
new_image = cv2.add(masked_background, masked_image_invers)

# Zusammenfassung der Ausganslage und der Bearbeitung
masked_image_invers = cv2.putText(masked_image_invers, 'Maskierung invers', (25, 25),
                                  font, 0.8, WHITE_3, 2, cv2.LINE_AA)
masked_background = cv2.putText(masked_background, 'Maskierung Hintergrund', (25, 25),
                                font, 0.8, WHITE_3, 2, cv2.LINE_AA)
new_image = cv2.putText(new_image, 'neues Bild', (25, 25),
                        font, 0.8, WHITE_3, 2, cv2.LINE_AA)

result = np.hstack([masked_image_invers, masked_background, new_image])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
