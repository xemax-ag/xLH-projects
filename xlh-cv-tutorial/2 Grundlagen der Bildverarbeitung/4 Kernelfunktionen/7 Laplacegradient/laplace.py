# laplace.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/sudoku.jpg')

# transformiere das Bild in den Graubereich
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# bestimme den Laplacegradienten
laplacian = cv2.Laplacian(image,cv2.CV_64F)

# Die Variable laplacian ist ein Array bestehend aus Fliesskommazahlen.
# Für die weiteren Schritte ist eine Typkonversation in uint8 notwendid.
print(laplacian)
# >>> float64
laplacian = cv2.convertScaleAbs(laplacian)
# >>> uint8

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
sobel_xy = cv2.putText(laplacian, 'Laplacegradient', (25, 25),
                       font, 0.8, WHITE, 2, cv2.LINE_AA)

result = np.hstack([image, laplacian])

# schreibe das Bild in eine Datei
cv2.imwrite('img/laplace.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
