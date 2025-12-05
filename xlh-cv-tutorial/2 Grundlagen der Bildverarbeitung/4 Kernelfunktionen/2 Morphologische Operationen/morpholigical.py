# morpholigical.py
import cv2
import imutils
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
BLACK = 0

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/fingerprint.png')
image = imutils.resize(image, height=300)
# Betrachtung als Graustufenbild
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Erodierung
image_eroded = image.copy()
image_eroded = cv2.putText(image_eroded, 'Original', (20, 20),
                           font, 0.8, BLACK, 2, cv2.LINE_AA)
for i in range(1, 4, 1):
    eroded = cv2.erode(image.copy(), None, iterations=i)
    eroded = cv2.putText(eroded, f'Erodierung {i:d}x', (20, 20),
                         font, 0.8, BLACK, 2, cv2.LINE_AA)
    image_eroded = np.hstack([image_eroded, eroded])

# Erweiterung
image_dilate = image.copy()
image_dilate = cv2.putText(image_dilate, 'Original', (20, 20),
                           font, 0.8, BLACK, 2, cv2.LINE_AA)
for i in range(1, 4, 1):
    dilate = cv2.dilate(image.copy(), None, iterations=i)
    dilate = cv2.putText(dilate, f'Erweiterung {i:d}x', (20, 20),
                         font, 0.8, BLACK, 2, cv2.LINE_AA)
    image_dilate = np.hstack([image_dilate, dilate])

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.vstack([image_eroded, image_dilate])

# schreibe das Bild in eine Datei
cv2.imwrite('img/morpholigical.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
