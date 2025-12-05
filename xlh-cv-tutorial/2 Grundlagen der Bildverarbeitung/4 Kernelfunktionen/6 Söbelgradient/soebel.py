# flipping.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/sudoku.jpg')

# transformiere das Bild in den Graubereich
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# bestimme die Soebelgradienten in Richtung X und Y
soebel_x = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=1, dy=0)
soebel_y = cv2.Sobel(image, ddepth=cv2.CV_64F, dx=0, dy=1)

# Die Variablen soebel_x und soebel_y sind Fliesskommazahlen.
# Für die weiteren Schritte ist eine Typkonversation in uint8 notwendid.
print(soebel_x.dtype, soebel_y.dtype)
# >>> float64 float64
soebel_x = cv2.convertScaleAbs(soebel_x)
soebel_y = cv2.convertScaleAbs(soebel_y)
print(soebel_x.dtype, soebel_y.dtype)
# >>> uint8 uint8

# Die Gradientenbilder in x und y Richtung werden zusammengefügt.
sobel_xy = cv2.addWeighted(soebel_x, 0.5, soebel_y, 0.5, 0)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, BLACK, 2, cv2.LINE_AA)
soebel_x = cv2.putText(soebel_x, 'Soebel X', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
soebel_y = cv2.putText(soebel_y, 'Soebel Y', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
sobel_xy = cv2.putText(sobel_xy, 'Resultat', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)

result = np.hstack([image, soebel_x, soebel_y, sobel_xy])

# schreibe das Bild in eine Datei
cv2.imwrite('img/soebel.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
