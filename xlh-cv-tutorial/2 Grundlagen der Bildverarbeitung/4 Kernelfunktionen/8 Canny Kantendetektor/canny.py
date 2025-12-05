# canny.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
GRAY = 127
BLACK = 0

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/sudoku.jpg')

# transformiere das Bild in den Graubereich
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Die hochfrequenten Anteile mittels Blurfilter entfernen.
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Canny Kantendedektor mit unterschiedlichen Grenzwerten.
canny_wide = cv2.Canny(blurred, 10, 200)
canny_mid = cv2.Canny(blurred, 30, 150)
canny_tight = cv2.Canny(blurred, 240, 250)

# Zusammenfassung der Ausganslage und der Bearbeitung
blurred = cv2.putText(blurred, 'Blurred', (25, 25), font, 0.8, GRAY, 2, cv2.LINE_AA)
canny_wide = cv2.putText(canny_wide, 'Canny wide', (25, 25),
                         font, 0.8, WHITE, 2, cv2.LINE_AA)
canny_mid = cv2.putText(canny_mid, 'Canny mid', (25, 25),
                        font, 0.8, WHITE, 2, cv2.LINE_AA)
canny_tight = cv2.putText(canny_tight, 'Canny tight', (25, 25),
                          font, 0.8, WHITE, 2, cv2.LINE_AA)
result = np.hstack([blurred, canny_wide, canny_mid, canny_tight])

# schreibe das Bild in eine Datei
cv2.imwrite('img/canny.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
