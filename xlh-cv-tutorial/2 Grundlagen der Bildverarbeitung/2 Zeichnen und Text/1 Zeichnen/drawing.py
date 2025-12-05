# drawing_1.py
import cv2
import numpy as np

# Farbdefintionen
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

# erstelle eine Leinwand mit der Breite 300, der Höhe 200 und Farbtiefe 3
canvas = np.zeros((200, 300, 3), dtype="uint8")
# Zuweisung der Farbe Weiss
canvas[0:-1, 0:-1] = WHITE

# oder mit direkter Farbvorgabe in der Initalisierung
# canvas = np.ones((200, 300, 3), dtype="uint8") * np.array((0, 0, 255), dtype='uint8')
# canvas = np.ones((200, 300, 3), dtype="uint8") * np.array(RED, dtype='uint8')

# Linie
cv2.line(canvas, (10, 10), (290, 190), RED, 5)
cv2.line(canvas, (10, 190), (290, 10), GREEN, 10)

# Rechteck
cv2.rectangle(canvas, (20, 20), (80, 60), BLUE, -1)  # - 1 => ausgefüllt
cv2.rectangle(canvas, (220, 140), (280, 180), BLUE, 3)

# Kreis
(center_x, center_y) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
for radius in range(0, 50, 5):
    cv2.circle(canvas, (center_x, center_y), radius, BLACK, 1)

# Elipse
for axes_y in range(0, 100, 10):
    cv2.ellipse(canvas, (center_x, center_y), (50, axes_y), 60, 0, 360, GREEN, 1)

# schreibe das Bild in eine Datei
cv2.imwrite('img/drawing_1.png', canvas[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', canvas)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
