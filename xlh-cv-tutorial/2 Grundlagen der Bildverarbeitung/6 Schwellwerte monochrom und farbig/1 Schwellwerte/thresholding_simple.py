# thresholding_simple.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0
WHITE_3 = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/coins.jpg')
# transformiere das Bild in den Graubereich
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blurfilter
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

tresh_val = 190

# Bei einem Grauwert des Pixels > tresh_val wird das Pixel auf Weiss gesetzt.
(T, threshold) = cv2.threshold(blurred, tresh_val, 255, cv2.THRESH_BINARY)

# Bei einem Grauwert des Pixels > tresh_val wird das Pixel Schwarz gesetzt.
(T, threshold_inv) = cv2.threshold(blurred, tresh_val, 255, cv2.THRESH_BINARY_INV)

# Maskierung vom Ursprungsbild mit dem Schwellwertbild
masked = cv2.bitwise_and(image, image, mask=threshold)
masked_inv = cv2.bitwise_and(image, image, mask=threshold_inv)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
blurred = cv2.putText(blurred, 'Blurred', (25, 50), font, 0.8, WHITE, 2, cv2.LINE_AA)
threshold = cv2.putText(threshold, 'Schwellwert', (50, 50),
                        font, 0.8, WHITE, 2, cv2.LINE_AA)
threshold_inv = cv2.putText(threshold_inv, 'Schwellwert invers', (50, 50),
                            font, 0.8, BLACK, 2, cv2.LINE_AA)
masked = cv2.putText(masked, 'Maskierung', (25, 25), font, 0.8, WHITE_3, 2, cv2.LINE_AA)
masked_inv = cv2.putText(masked_inv, 'Maskierung invers', (25, 25),
                         font, 0.8, WHITE_3, 2, cv2.LINE_AA)
result_1 = np.hstack([blurred, threshold, threshold_inv])
result_2 = np.hstack([image, masked, masked_inv])

# schreibe das Bild in eine Datei
cv2.imwrite('img/thresholding_simple_1.png', result_1[0:-2, 0:-2])
cv2.imwrite('img/thresholding_simple_2.png', result_2[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe 1', result_1)
cv2.imshow('Ausgabe 2', result_2)
cv2.moveWindow('Ausgabe 1', 100, 100)
cv2.moveWindow('Ausgabe 2', 100, 500)
cv2.waitKey(0)
