# masking.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/contours.png')[4:-4, 4:-4]
white = np.ones(image.shape, dtype="uint8") * 255
black = np.zeros(image.shape, dtype="uint8")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# finde alle Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
conturs_all = image.copy()
cv2.drawContours(conturs_all, cnts, -1, GREEN, 2)

# Maskierung der Konturen
masking = np.zeros(gray.shape, dtype="uint8")  # schwarze Leinwand
cv2.drawContours(masking, cnts, -1, 255, -1)
masked_in = cv2.bitwise_not(black, mask=masking)

# Maskierung des Hintergrundes
masking = np.ones(gray.shape, dtype="uint8")*255  # weisse Leinwand
cv2.drawContours(masking, cnts, -1, 0, -1)
masked_back = cv2.bitwise_not(black, mask=masking)

# Zusammenfassung der Ausganslage und der Bearbeitung
conturs_all = cv2.putText(conturs_all, 'alle Konturen', (25, 25),
                          font, 0.8, WHITE, 2, cv2.LINE_AA)
masked_in = cv2.putText(masked_in, 'Maskierung der Konturen', (25, 25),
                        font, 0.8, WHITE, 2, cv2.LINE_AA)
masked_back = cv2.putText(masked_back, 'Maskierung des Hintergrundes', (25, 25),
                          font, 0.8, BLACK, 2, cv2.LINE_AA)
result = np.hstack([conturs_all, masked_in, masked_back])

# schreibe das Bild in eine Datei
cv2.imwrite('img/masking.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
