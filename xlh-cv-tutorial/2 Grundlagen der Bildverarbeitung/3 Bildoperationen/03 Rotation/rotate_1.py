# rotate_1.py
import cv2
import imutils
import numpy as np


# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Rotation um -30 Grad (Uhrzeigersinn) im Bildzentrum
rotated = imutils.rotate(image, -30)

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.hstack([image, rotated])

# schreibe das Bild in eine Datei
cv2.imwrite('img/rotate_1.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
