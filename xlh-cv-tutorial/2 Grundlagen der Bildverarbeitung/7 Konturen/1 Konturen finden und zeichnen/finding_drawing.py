# finding_drawing.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/contours.png')[4:-4, 4:-4]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# finde alle Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
conturs_all = image.copy()
cv2.drawContours(conturs_all, cnts, -1, (0, 255, 0), 2)

# finde alle äusseren Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conturs_external = image.copy()
cv2.drawContours(conturs_external, cnts, -1, (0, 255, 0), 2)

# finde alle inneren Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(gray.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print(hir)
# >>> [[ 2 -1  1 -1]
# >>>  [-1 -1 -1  0]
# >>>  [ 4  0  3 -1]
# >>>  [-1 -1 -1  2]
# >>>  [ 5  2 -1 -1]
# >>>  [ 6  4 -1 -1]
# >>>  [-1  5 -1 -1]]
conturs_internal = image.copy()
for (i, c) in enumerate(cnts):
    if hir[0][i][3] >= 0:
        cv2.drawContours(conturs_internal, [c], -1, GREEN, 2)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
conturs_all = cv2.putText(conturs_all, 'alle Konturen', (25, 25),
                          font, 0.8, WHITE, 2, cv2.LINE_AA)
conturs_external = cv2.putText(conturs_external, 'aeussere Konturen', (25, 25),
                               font, 0.8, WHITE, 2, cv2.LINE_AA)
conturs_internal = cv2.putText(conturs_internal, 'innere Konturen', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)

result_1 = np.hstack([image, conturs_all])
result_2 = np.hstack([conturs_external, conturs_internal])
result = np.vstack([result_1, result_2])

# schreibe das Bild in eine Datei
cv2.imwrite('img/finding_drawing.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
