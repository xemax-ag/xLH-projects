# cropping.py
import cv2
import numpy as np
import imutils

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Zuschneiden des Bildes mit NumPy Arraymanipulationen
croped = image[175:-100, 125:-100]

# schreibe das Bild in eine Datei
cv2.imwrite('img/cropping.png', croped[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', croped)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
