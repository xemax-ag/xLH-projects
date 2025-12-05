# blurring.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
RED = (0, 0, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Kernelgrössen
kernel_sizes = [(5, 5), (11, 11), (19, 19)]

# Mittelwertfilter cv2.blur
image_blurred = image.copy()
image_blurred = cv2.putText(image_blurred, 'Original', (25, 25),
                            font, 0.8, RED, 2, cv2.LINE_AA)
for (x, y) in kernel_sizes:
    blurred = cv2.blur(image, (x, y))
    blurred = cv2.putText(blurred, f'Mittelwertfilter ({x:d}, {y:d})', (25, 25),
                          font, 0.8, RED, 2, cv2.LINE_AA)
    image_blurred = np.hstack([image_blurred, blurred])

# Gaussfilter cv2.GaussianBlur
image_gaussian = image.copy()
image_gaussian = cv2.putText(image_gaussian, 'Original', (25, 25),
                             font, 0.8, RED, 2, cv2.LINE_AA)
for (x, y) in kernel_sizes:
    blurred = cv2.GaussianBlur(image, (x, y), 0)
    blurred = cv2.putText(blurred, f'Gaussfilter ({x:d}, {y:d})', (25, 25),
                          font, 0.8, RED, 2, cv2.LINE_AA)
    image_gaussian = np.hstack([image_gaussian, blurred])

# Medianfilter cv2.medianBlur
image_median = image.copy()
image_median = cv2.putText(image_median, 'Original', (25, 25),
                           font, 0.8, RED, 2, cv2.LINE_AA)
for (x, y) in kernel_sizes:
    blurred = cv2.medianBlur(image, x)
    blurred = cv2.putText(blurred, f'Medianfilter ({x:d})', (25, 25),
                          font, 0.8, RED, 2, cv2.LINE_AA)
    image_median = np.hstack([image_median, blurred])

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.vstack([image_blurred, image_gaussian, image_median])

# schreibe das Bild in eine Datei
cv2.imwrite('img/blurring.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
