# pixel_basics.py
import cv2
import numpy as np


image = cv2.imread('img/OpenCV_logo_with_text.png')
(height, width) = image.shape[:2]
cv2.imshow('Originalbild', image)
print('width:', width, 'height:', height, 'numpy.shape:', np.shape(image))

# Bilder werden als NumPy Arrays interpretiert.
(b, g, r) = image[235, 111]
print(f'Pixel (111, 235) - Rot: {r:d}, Grün: {g:d}, Blau: {b:d}')

# das Pixel an der Koordinate (5, 10) wird Blau eingefärbt
image[10, 5] = (255, 0, 0)
(b, g, r) = image[10, 5]
print(f'Pixel (5, 10) - Rot: {r:d}, Grün: {g:d}, Blau: {b:d}')

# Bestimmung des Bildzentrums
(center_X, center_Y) = (width // 2, height // 2)

# NumPy erlaubt es auf einfache Weise Bildausschnitte zu separieren
top_left = image[0:center_Y, 0:center_X]
cv2.imshow('Subimage oben-links', top_left)

# im gleichen Stil
top_right = image[0:center_Y, center_X:width]
bottom_right = image[center_Y:height, center_X:width]
bottom_left = image[center_Y:height, 0:center_X]
cv2.imshow('Subimage oben-rechts', top_right)
cv2.imshow('Subimage unten-rechts', bottom_right)
cv2.imshow('Subimage unten-links', bottom_left)

# Durch einfache Zuweisung lassen sich Bereiche einfärben => Pink.
image[0:center_Y, 0:center_X] = (255, 0, 255)

# Anzeige auf dem Bildschirm
cv2.imshow('Bearbeitetes Bild', image)
cv2.waitKey(0)
