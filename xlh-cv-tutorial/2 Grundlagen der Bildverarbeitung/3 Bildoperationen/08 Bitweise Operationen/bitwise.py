# bitwise.py
import cv2
import numpy as np
import imutils

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
BLACK = 0


# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')
# Transformation des Bildes in den Graubereich (siehe Kapitel Farbräume)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Rechteck in der Farbe Schwarz (0 => 1 Dimension)
rectangle = np.zeros(np.shape(image), dtype="uint8")


# Kreis in der Farbe Weiss (255 => 1 Dimension)
circle = np.zeros(np.shape(image), dtype="uint8")
center_x = np.shape(image)[1] // 2
center_y = np.shape(image)[0] // 2
cv2.circle(circle, (center_x, center_y), 125, 255, -1)

# Bitweises AND
bitwise_and_1 = cv2.bitwise_and(image, rectangle)
bitwise_and_1 = cv2.putText(bitwise_and_1, 'cv2.bitwise_and', (40, 40),
                            font, 1.0, WHITE, 2, cv2.LINE_AA)
bitwise_and_2 = cv2.bitwise_and(image, circle)
bitwise_and_2 = cv2.putText(bitwise_and_2, 'cv2.bitwise_and', (40, 40),
                            font, 1.0, WHITE, 2, cv2.LINE_AA)

# Bitweises ODER
bitwise_or_1 = cv2.bitwise_or(image, rectangle)
bitwise_or_1 = cv2.putText(bitwise_or_1, 'cv2.bitwise_or', (40, 40),
                           font, 1.0, WHITE, 2, cv2.LINE_AA)
bitwise_or_2 = cv2.bitwise_or(image, circle)
bitwise_or_2 = cv2.putText(bitwise_or_2, 'cv2.bitwise_or', (40, 40),
                           font, 1.0, WHITE, 2, cv2.LINE_AA)

# Bitweises XOR
bitwise_xor_1 = cv2.bitwise_xor(image, rectangle)
bitwise_xor_1 = cv2.putText(bitwise_xor_1, 'cv2.bitwise_xor', (40, 40),
                            font, 1.0, WHITE, 2, cv2.LINE_AA)
bitwise_xor_2 = cv2.bitwise_xor(image, circle)
bitwise_xor_2 = cv2.putText(bitwise_xor_2, 'cv2.bitwise_xor', (40, 40),
                            font, 1.0, WHITE, 2, cv2.LINE_AA)

# Bitweises NOT
bitwise_not = cv2.bitwise_not(circle)
bitwise_not = cv2.putText(bitwise_not, 'cv2.bitwise_NOT', (40, 40),
                          font, 1.0, BLACK, 2, cv2.LINE_AA)



# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (40, 40), font, 1.0, WHITE, 2, cv2.LINE_AA)
rectangle = cv2.putText(rectangle, 'Rechteck', (40, 40), font, 1.0, WHITE, 2, cv2.LINE_AA)
circle = cv2.putText(circle, 'Kreis', (40, 40), font, 1.0, WHITE, 2, cv2.LINE_AA)
result_1 = np.hstack([image, rectangle, bitwise_and_1, bitwise_or_1, bitwise_xor_1])
result_2 = np.hstack([image, circle, bitwise_and_2, bitwise_or_2, bitwise_xor_2])
retangle_black = np.zeros(np.shape(image), dtype="uint8")
result_3 = np.hstack([circle, bitwise_not, retangle_black, retangle_black, retangle_black])
result = np.vstack([result_1, result_2, result_3])

# schreibe das Bild in eine Datei
cv2.imwrite('img/bitwise.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
