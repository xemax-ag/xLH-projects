# properties.py
import cv2
import numpy as np

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/contours.png')[4:-4, 4:-4]
black = np.zeros(image.shape, dtype="uint8")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# finde alle äusseren Konturen und zeichne diese in das Bild
cnts, hir = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conturs_external = image.copy()
cv2.drawContours(conturs_external, cnts, -1, (0, 255, 0), 2)

# loop over the contours
center_of_mass = image.copy()
for c in cnts:
    # compute the moments of the contour which can be used to compute the
    # centroid or 'center of mass' of the region
    M = cv2.moments(c)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    # draw the center of the contour on the image
    cv2.circle(center_of_mass, (cX, cY), 10, GREEN, -1)

# loop over the contours
area_perimeter = image.copy()
for (i, c) in enumerate(cnts):
    # compute the area and the perimeter of the contour
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print(f'Contour #{(i+1):d} -- area: {area:.2f}, perimeter: {perimeter:.2f}')
    # draw the contour on the image
    cv2.drawContours(area_perimeter, [c], -1, GREEN, 2)
    # compute the center of the contour and draw the contour number
    M = cv2.moments(c)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    cv2.putText(area_perimeter, f'#{(i+1):d}', (cX - 20, cY),
                font, 0.8, RED, 2, cv2.LINE_AA)
# >>> Contour #1 -- area: 3213.00, perimeter: 264.31
# >>> Contour #2 -- area: 2412.00, perimeter: 237.28
# >>> Contour #3 -- area: 5293.50, perimeter: 324.84
# >>> Contour #4 -- area: 5514.50, perimeter: 337.95
# >>> Contour #5 -- area: 6954.00, perimeter: 312.74
# >>> Contour #6 -- area: 10411.00, perimeter: 454.48
# >>> Contour #7 -- area: 5982.50, perimeter: 513.04
# >>> Contour #8 -- area: 2491.50, perimeter: 310.09

# bounding Box
bounding_box = image.copy()
for c in cnts:
    # fit a bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(bounding_box, (x, y), (x + w, y + h), GREEN, 2)

# bounding Box gedreht
bounding_box_rotated = image.copy()
for c in cnts:
    box = cv2.minAreaRect(c)
    box = np.int64(cv2.boxPoints(box))
    cv2.drawContours(bounding_box_rotated, [box], -1, GREEN, 2)

# minimaler Umfangskreis
min_enclosing_circle = image.copy()
for c in cnts:
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(min_enclosing_circle, (int(x), int(y)), int(radius), GREEN, 2)

# minimale Umfangsellipse
min_enclosing_elipse = image.copy()
for c in cnts:
    # eine Ellipse braucht mindestens 5 Punkte
    if len(c) >= 5:
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(min_enclosing_elipse, ellipse, GREEN, 2)


# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
conturs_external = cv2.putText(conturs_external, 'aeussere Konturen', (25, 25),
                               font, 0.8, WHITE, 2, cv2.LINE_AA)
center_of_mass = cv2.putText(center_of_mass, 'Massezentrum', (25, 25),
                             font, 0.8, WHITE, 2, cv2.LINE_AA)
area_perimeter = cv2.putText(area_perimeter, 'Flaeche und Umfang', (25, 25),
                             font, 0.8, WHITE, 2, cv2.LINE_AA)
bounding_box = cv2.putText(bounding_box, 'bounding Box', (25, 25),
                           font, 0.8, WHITE, 2, cv2.LINE_AA)
bounding_box_rotated = cv2.putText(bounding_box_rotated, 'bounding Box gedreht',
                                   (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
min_enclosing_circle = cv2.putText(min_enclosing_circle, 'minimaler Umfangskreis',
                                   (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
min_enclosing_elipse = cv2.putText(min_enclosing_elipse, 'minimale Umfangsellipse',
                                   (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
result_1 = np.hstack([image, conturs_external, center_of_mass])
result_2 = np.hstack([area_perimeter, bounding_box, bounding_box_rotated])
result_3 = np.hstack([min_enclosing_circle, min_enclosing_elipse, black])
result = np.vstack([result_1, result_2, result_3])

# schreibe das Bild in eine Datei
cv2.imwrite('img/properties.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
