# Konturen finden und zeichnen
Die vorhergehenden Lektionen zeigten Möglichkeiten wie Schwellwerte und Kantendetektion.  
Die zentrale Frage besteht darin, wie können die Eigenschaften der Konturen (Fläche, Umfang, Koordinaten) zugänglich 
gemacht werden.
 
# cv2.findContours
Der Konturenalgorithmus von OpenCV erlaubt die Detektion und Erfassung unterschiedlicher Eigenschaften.  

````python
# Graustufenbild
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
````

Weitere Informationen sind der OpenCV Dokumentation zu entnehmen:  
[Contours in OpenCV](https://docs.opencv.org/4.2.0/d3/d05/tutorial_py_table_of_contents_contours.html)
