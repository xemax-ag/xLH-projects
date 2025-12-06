# Bitoperationen
Die Bitoperationen 
* AND
* OR
* XOR
* NOT

ermöglichen die logischen Operationen in Bildern.
In dieser Lektion werden eindimensionale Bilder (Graustufenbilder) betrachtet. Die Betrachtung
von Farbbildern (dreidimensional) erfolgt in der Lektion Maskierungen.

# Farbkonvertierung
Die Konvertierung in unterschiedliche Farbräume (siehe auch Lektion Farbräume) erfolgt durch die 
Funktion `cv2.cvtColor` der zweite Parameter bestimmt den Zielfarbraum.

````python
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Graustufenkonvertierung
````

Hinweis: Weitere Konvertierungen sind der 
[OpenCV Dokumentation ](https://docs.opencv.org/4.2.0/d8/d01/group__imgproc__color__conversions.html)
zu entnehmen.
