import cv2
import numpy as np
from skimage.filters import threshold_local

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
RED = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (0, 255, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/domino_1.jpg')[4:-4, 4:-4]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blurfilter
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Bei einem Pixelwert > 100 wird das Pixel auf Weiss gesetzt.
(T, threshold) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

# adaptive Schwellwertbetrachtung
T = threshold_local(blurred, 199, offset=0, method="gaussian")
threshold_adaptive = (blurred >= T).astype("uint8") * 255

# Morphologische Operationen
eroded = cv2.erode(threshold, None, iterations=2)
dilated = cv2.dilate(eroded, None, iterations=2)

# Erstelle eine Kopie der Bildes in welchem die Vorverararbeitungen durchgeführt wurden.
# Dies ist wichtig, weil die Konturenoperationen das Ursprungsbild verändern.
image_to_contours = dilated.copy()

# finde alle Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(image_to_contours.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours_all = image.copy()
cv2.drawContours(contours_all, cnts, -1, (0, 255, 0), 2)

# finde alle äusseren Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(image_to_contours.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_external = image.copy()
cv2.drawContours(contours_external, cnts, -1, (0, 255, 0), 2)

# finde alle inneren Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(image_to_contours.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours_internal = image.copy()
for (i, c) in enumerate(cnts):
    if hir[0][i][3] >= 0:
        M = cv2.moments(c)
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
        # Fläche und Umfang
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        print(f'Contour #{(i + 1):d} -- area: {area:.2f}, perimeter: {perimeter:.2f}')

        # draw the center of the contour on the image
        cv2.circle(contours_internal, (cX, cY), 10, GREEN, -1)

        if area < 5000:
            # minimaler Umfgangskreis
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            cv2.circle(contours_internal, (cX, cY), int(radius), RED, 2)
            # speichern der Punktkoordinaten
        else:
            cv2.drawContours(contours_internal, [c], -1, YELLOW, 4)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, RED, 2, cv2.LINE_AA)
gray = cv2.putText(gray, 'Graustufenbild', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
blurred = cv2.putText(blurred, 'Unschaerfe', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
threshold = cv2.putText(threshold, 'Schwellwert', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
threshold_adaptive = cv2.putText(threshold_adaptive, 'adaptiver Schwellwert', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
eroded = cv2.putText(eroded, 'Reduzierung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
contours_all = cv2.putText(contours_all, 'alle Konturen', (25, 25), font, 0.8, RED, 2, cv2.LINE_AA)
contours_external = cv2.putText(contours_external, 'aeussere Konturen', (25, 25), font, 0.8, RED, 2, cv2.LINE_AA)
contours_internal = cv2.putText(contours_internal, 'innere Konturen', (25, 25), font, 0.8, RED, 2, cv2.LINE_AA)


result_1 = np.hstack([image, contours_all])
result_2 = np.hstack([contours_external, contours_internal])
# result_3 = np.hstack([])
result_4 = np.hstack([gray, blurred])
result_5 = np.hstack([threshold, threshold_adaptive])
result_6 = np.hstack([eroded, dilated])

result_stack_color = np.vstack([result_1, result_2])
result_stack_mono = np.vstack([result_4, result_5, result_6])

# schreibe das Bild in eine Datei
cv2.imwrite('img/contours_c.png', result_stack_color[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe_farbig', result_stack_color)
cv2.moveWindow('Ausgabe_farbig', 100, 100)
# cv2.imshow('Ausgabe_monochrom', result_stack_mono)
# cv2.moveWindow('Ausgabe_monochrom', 100, 460)
cv2.waitKey(0)
