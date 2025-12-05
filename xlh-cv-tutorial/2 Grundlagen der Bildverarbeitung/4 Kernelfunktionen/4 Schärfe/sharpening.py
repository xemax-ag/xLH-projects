# sharpening.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
RED = (0, 0, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Kernelgrössen
kernel_sizes = [(5, 5), (11, 11), (19, 19)]

# Helligkeitsoffset
offset = 0

# Mittelwertfilter cv2.blur
image_blurred = image.copy()
image_blurred = cv2.putText(image_blurred, 'Original', (25, 25),
                            font, 0.8, RED, 2, cv2.LINE_AA)

image_sharpened = image.copy()
image_sharpened = cv2.putText(image_blurred, 'Original', (25, 25),
                              font, 0.8, RED, 2, cv2.LINE_AA)

for (x, y) in kernel_sizes:
    blurred = cv2.blur(image, (x, y))
    sharpened = cv2.addWeighted(image, 2, blurred, -1, offset)
    blurred = cv2.putText(blurred, f'Mittelwertfilter ({x:d}, {y:d})', (25, 25),
                          font, 0.8, RED, 2, cv2.LINE_AA)
    sharpened = cv2.putText(sharpened, f'Schaerfe ({x:d}, {y:d})', (25, 25),
                            font, 0.8, RED, 2, cv2.LINE_AA)
    image_blurred = np.hstack([image_blurred, blurred])
    image_sharpened = np.hstack([image_sharpened, sharpened])

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.vstack([image_blurred, image_sharpened])

# schreibe das Bild in eine Datei
cv2.imwrite('img/sharpening.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
