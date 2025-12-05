# pixel_basics.py
import cv2
import numpy as np

image = cv2.imread('img/python_snake.jpg')
(height, width) = image.shape[:2]
cv2.imshow('Originalbild', image)
print('width:', width, 'height:', height, 'numpy.shape:', np.shape(image))

# Bestimmung der RGB Werte eines Bildpixels
(pixel_x, pixel_y) = (100, 560)
(b, g, r) = image[pixel_y, pixel_x]
print(f'Pixel ({pixel_x:d}, {pixel_y}) - Rot: {r:d}, Grün: {g:d}, Blau: {b:d}')