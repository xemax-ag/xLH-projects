# Kontureneigenschaften
Nach der Erfassung der Konturen stehen unterschiedliche weitere Funktionen zur Weiterverarbeitung zur Verfügung.

## Massenzentrum 
Erfassung des Massenzentrums
````python
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
```` 

## Fläche und Umfang
````python
# loop over the contours
area_perimeter = image.copy()
for (i, c) in enumerate(cnts):
    # compute the area and the perimeter of the contour
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print(f'Contour #{(i+1):d} -- area: {area:.2f}, perimeter: {perimeter:.2f}')
````

## Begrenzungsrahmen (Bounding Box)
````python
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
````

## Minimaler Umfangskreis
````python
# minimaler Umfangskreis
min_enclosing_circle = image.copy()
for c in cnts:
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(min_enclosing_circle, (int(x), int(y)), int(radius), GREEN, 2)
````

## Minimale Umfangsellipse
````python
# minimale Umfangsellipse
min_enclosing_elipse = image.copy()
for c in cnts:
    # eine Ellipse braucht mindestens 5 Punkte
    if len(c) >= 5:
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(min_enclosing_elipse, ellipse, GREEN, 2)
````
