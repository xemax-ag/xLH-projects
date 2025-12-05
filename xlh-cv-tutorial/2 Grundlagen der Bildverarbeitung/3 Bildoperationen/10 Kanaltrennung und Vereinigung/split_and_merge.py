# split_and_merge.py
import cv2
import numpy as np
import imutils

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
WHITE_3 = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Auftrennung der Farbkanäle
(blue, green, red) = cv2.split(image)

# Zusammenführung der Farbkanäle
merged = cv2.merge([blue, green, red])

# Beschriftund der Bilder
image = cv2.putText(image, 'Original', (25, 25),
                    font, 0.8, WHITE_3, 2, cv2.LINE_AA)
merged = cv2.putText(merged, 'RGB Vereinigung', (25, 25),
                     font, 0.8, WHITE_3, 2, cv2.LINE_AA)
blue = cv2.putText(blue, 'Blaukanal', (25, 25),
                   font, 0.8, WHITE, 2, cv2.LINE_AA)
green = cv2.putText(green, 'Gruenkanal', (25, 25),
                    font, 0.8, WHITE, 2, cv2.LINE_AA)
red = cv2.putText(red, 'Rotkanal', (25, 25),
                  font, 0.8, WHITE, 2, cv2.LINE_AA)

# Zusammenfassung der Ausganslage und der Bearbeitung
result_1 = np.hstack([image, merged])
result_2 = np.hstack([blue, green, red])

# schreibe das Bild in eine Datei
cv2.imwrite('img/split_and_merge_1.png', result_1[0:-2, 0:-2])
cv2.imwrite('img/split_and_merge_2.png', result_2[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe 1', result_1)
cv2.moveWindow('Ausgabe 1', 100, 100)

cv2.imshow('Ausgabe 2', result_2)
cv2.moveWindow('Ausgabe 2', 900, 100)

cv2.waitKey(0)
