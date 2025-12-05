import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE_3 = (255, 255, 255)
BLACK_3 = (0, 0, 0)
WHITE = 255
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# öffne das Bild
image = cv2.imread('img/edge_detector.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Die hochfrequenten Anteile mittels Blurfilter entfernen.
blurred = cv2.GaussianBlur(image_gray, (9, 9), 0)

# Canny Kantendedektor mit unterschiedlichen Grenzwerten.
canny = cv2.Canny(blurred, 0, 20)

# Dilate
dilated = cv2.dilate(canny, None, iterations=1)

# finde alle äusseren Konturen und markiere diese im Bild
cnts, hir = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conturs = image.copy()
cv2.drawContours(conturs, cnts, -1, GREEN, 2)

# loop über die einzelnen Konturen
min_circle = image.copy()
for (i, c) in enumerate(cnts):
    # berechne
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    # print(x, y, radius)
    if radius > 15:
        # zeichne den Kreis
        cv2.circle(min_circle, (int(x), int(y)), 5, RED, -1)
        cv2.circle(min_circle, (int(x), int(y)), int(radius), RED, 2)

image_gray = cv2.putText(image_gray, 'Graubild', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
canny = cv2.putText(canny, 'Canny Kantenfilter', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, BLACK_3, 2, cv2.LINE_AA)
conturs = cv2.putText(conturs, 'Konturen', (25, 25), font, 0.8, BLACK_3, 2, cv2.LINE_AA)
min_circle = cv2.putText(min_circle, 'Resultat', (25, 25), font, 0.8, BLACK_3, 2, cv2.LINE_AA)
result_1 = np.hstack([image_gray, canny, dilated])
result_2 = np.hstack([image, conturs, min_circle])


# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe 1', result_1)
cv2.imshow('Ausgabe 2', result_2)
cv2.moveWindow('Ausgabe 1', 100, 100)
cv2.moveWindow('Ausgabe 2', 100, 440)
cv2.waitKey(0)
