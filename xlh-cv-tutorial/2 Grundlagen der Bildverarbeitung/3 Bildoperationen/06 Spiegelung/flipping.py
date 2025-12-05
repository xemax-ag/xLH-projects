# flipping.py
import cv2
import numpy as np
import imutils

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Spiegelung horizontal
flipped_h = cv2.flip(image, 1)

# Spiegelung vertikal
flipped_v = cv2.flip(image, 0)

# Spiegelung horizontal und vertikal
flipped_hv = cv2.flip(image, -1)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
flipped_h = cv2.putText(flipped_h, 'horizontal', (25, 25),
                        font, 0.8, WHITE, 2, cv2.LINE_AA)
flipped_v = cv2.putText(flipped_v, 'vertikal', (25, 25),
                        font, 0.8, WHITE, 2, cv2.LINE_AA)
flipped_hv = cv2.putText(flipped_hv, 'horizontal und vertikal', (25, 25),
                         font, 0.8, WHITE, 2, cv2.LINE_AA)
result = np.hstack([image, flipped_h, flipped_v, flipped_hv])

# schreibe das Bild in eine Datei
cv2.imwrite('img/flipping.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
