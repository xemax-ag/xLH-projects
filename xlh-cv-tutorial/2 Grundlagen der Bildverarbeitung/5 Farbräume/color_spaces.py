# color_spaces.py
import cv2
import numpy as np
import imutils

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image_bgr = cv2.imread('img/box_with_bullets.png')
# Zerlegung in die B G R Komponenten
(image_b, image_g, image_r) = cv2.split(image_bgr)

# Konvertierung in den HSV Farbraum
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
# Zerlegung in die H S V Komponenten
(image_h, image_s, image_v) = cv2.split(image_hsv)
print(image_h, np.max(image_h))

# Konvertierung in den LAB Farbraum
image_lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
# Zerlegung in die L A B Komponenten
(image_l, image_a, image_b2) = cv2.split(image_lab)

# Zusammenfassung der Ausganslage und der Bearbeitung
image_bgr = cv2.putText(image_bgr, 'BGR', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_b = cv2.putText(image_b, 'BGR Kanal B', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_g = cv2.putText(image_g, 'BGR Kanal G', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_r = cv2.putText(image_r, 'BGR Kanal R', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_hsv = cv2.putText(image_hsv, 'HSV', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_h = cv2.putText(image_h, 'HSV Kanal H', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_s = cv2.putText(image_s, 'HSV Kanal S', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_v = cv2.putText(image_v, 'HSV Kanal V', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_lab = cv2.putText(image_lab, 'LAB', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_l = cv2.putText(image_l, 'LAB Kanal L', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_a = cv2.putText(image_a, 'LAB Kanal A', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image_b2 = cv2.putText(image_b2, 'LAB Kanal B', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)

result = np.hstack([image_bgr, image_hsv, image_lab])
result_bgr = np.hstack([image_b, image_g, image_r])
result_hsv = np.hstack([image_h, image_s, image_v])
result_lab = np.hstack([image_l, image_a, image_b2])
result_bgr_hsv_lab = np.vstack([result_bgr, result_hsv, result_lab])

# schreibe das Bild in eine Datei
cv2.imwrite('img/color_spaces.png', result[0:-2, 0:-2])
cv2.imwrite('img/result_bgr_hsv_lab.png', result_bgr_hsv_lab[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.imshow('Ausgabe BGR HSV LAB', result_bgr_hsv_lab)
cv2.moveWindow('Ausgabe BGR HSV LAB', 100, 500)
cv2.waitKey(0)
