import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
RED = (0, 0, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/domino_1.jpg')[4:-4, 4:-4]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blurfilter
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, RED, 2, cv2.LINE_AA)
gray = cv2.putText(gray, 'Graustufenbild', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
blurred = cv2.putText(blurred, 'Unschaerfe', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
result_1 = np.hstack([image])
result_2 = np.hstack([gray, blurred])

# schreibe das Bild in eine Datei
cv2.imwrite('img/blur.png', result_2[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe_farbig', result_1)
cv2.moveWindow('Ausgabe_farbig', 100, 100)
cv2.imshow('Ausgabe_monochrom', result_2)
cv2.moveWindow('Ausgabe_monochrom', 100, 460)
cv2.waitKey(0)
