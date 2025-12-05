# masking.py
import cv2
import numpy as np
import imutils

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# bestimme den Bildmittelpunkt
center_x = np.shape(image)[1] // 2
center_y = np.shape(image)[0] // 2

# Die Maske muss die gleichen Abmasse in Breite und Höhe wie das Vergleichsbild aufweisen.
mask = np.zeros(image.shape[:2], dtype="uint8")

# Rechteckmaske => wichtig ist die Uebergabe einer Kopie des Maskierungsarrays
mask_rectangle = cv2.rectangle(mask.copy(), ((center_x-100), (center_y-100)),
                               ((center_x+100), (center_y+100)), 255, -1)

# Kreismaske => wichtig ist die Uebergabe einer Kopie des Maskierungsarrays
mask_circle = cv2.circle(mask.copy(), ((center_x), (center_y)), 100, 255, -1)

# Anwendung der Masken auf das Bild
masked_rectangle = cv2.bitwise_and(image, image, mask=mask_rectangle)
masked_circle = cv2.bitwise_and(image, image, mask=mask_circle)

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.hstack([image, masked_rectangle, masked_circle])

# schreibe das Bild in eine Datei
cv2.imwrite('img/masking.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
