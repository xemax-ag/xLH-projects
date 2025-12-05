# resize.py
import cv2
import numpy as np
import imutils

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets_original.jpg')
print(np.shape(image))
# >>> (2728, 2728, 3)

# Grössenänderung auf eine Breite
resized = imutils.resize(image, width=640)
print(np.shape(resized))
# >>> (640, 640, 3)

# schreibe das Bild in eine Datei
cv2.imwrite('img/resize.png', resized[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', resized)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
