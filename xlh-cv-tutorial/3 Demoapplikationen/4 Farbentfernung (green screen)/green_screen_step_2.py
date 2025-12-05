# green_screen_step_2.py
import cv2
import numpy as np
import imutils

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0
WHITE_3 = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/green_screen.png')
image = imutils.resize(image, width=480)

# Gaussian Blurfilter
blurred = cv2.GaussianBlur(image, (9, 9), 0)

# transformiere das Bild in den HSV Bereich
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Schwellwertbetrachtung
threshold_color = cv2.inRange(image_hsv, (45, 0, 0), (85, 255, 255))

# Erodieruqng, Dilate
eroded = cv2.erode(threshold_color, None, iterations=2)
dilated = cv2.dilate(eroded, None, iterations=2)
dilated_not = cv2.bitwise_not(dilated)

# Maskierung vom Ursprungsbild mit dem Schwellwertbild
masked_image = cv2.bitwise_and(image, image, mask=dilated)
masked_image_invers = cv2.bitwise_and(image, image, mask=dilated_not)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
masked_image = cv2.putText(masked_image, 'Maskierung', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
masked_image_invers = cv2.putText(masked_image_invers, 'Maskierung invers', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
threshold_color = cv2.putText(threshold_color, 'Schwellwert', (25, 25),
                              font, 0.8, BLACK, 2, cv2.LINE_AA)
eroded = cv2.putText(eroded, 'Erodierung', (25, 25), font, 0.8, BLACK, 2, cv2.LINE_AA)
dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, BLACK, 2, cv2.LINE_AA)
result_1 = np.hstack([threshold_color, eroded, dilated])
result_2 = np.hstack([image, masked_image, masked_image_invers])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe 1', result_1)
cv2.imshow('Ausgabe 2', result_2)
cv2.moveWindow('Ausgabe 1', 100, 100)
cv2.moveWindow('Ausgabe 2', 100, 425)
cv2.waitKey(0)
