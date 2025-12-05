# translate.py
import cv2
import imutils
import numpy as np


# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# verschiebe das Bild um 150 Pixel nach rechts und 50 nach unten
shifted = imutils.translate(image, 150, 50)

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.hstack([image, shifted])

# schreibe das Bild in eine Datei
cv2.imwrite('img/translate.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
