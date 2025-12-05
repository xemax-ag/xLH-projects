# text.py
import cv2
import numpy as np

# Farbdefintionen
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# erstelle eine Leinwand mit der Breite 300, der Höhe 200 und Farbtiefe 3
canvas = np.zeros((200, 300, 3), dtype="uint8")

# Zuweisung der Farbe Weiss
canvas[0:-1, 0:-1] = WHITE

# definiere den Font
font = cv2.FONT_HERSHEY_SIMPLEX

# schreibe auf die Leinwand
image = cv2.putText(canvas, 'Text 1', (50, 50),
                    font, 0.5, RED, 1, cv2.LINE_AA)
image = cv2.putText(canvas, 'Text 2', (50, 100),
                    font, 0.75, GREEN, 2, cv2.LINE_AA)
image = cv2.putText(canvas, 'OpenCV', (50, 150),
                    font, 1.0, BLACK, 3, cv2.LINE_AA, False)
image = cv2.putText(canvas, 'OpenCV', (50, 150),
                    font, 1.0, BLACK, 3, cv2.LINE_AA, True)

# schreibe das Bild in eine Datei
cv2.imwrite('img/text.png', canvas[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', canvas)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
