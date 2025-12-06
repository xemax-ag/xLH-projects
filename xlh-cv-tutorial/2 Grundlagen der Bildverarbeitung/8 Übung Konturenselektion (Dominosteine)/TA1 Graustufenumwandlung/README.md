# TA1 Graustufenumwandlung

## Aufgabe
Umwandlung des Farbbildes in ein Graustufenbild

## Hintergrundinformationen
Bei der Konturenselektion wird eine Suche nach Farbübergangen (Schwarz und Weiss sind auch Farben) mittels 
Algorithmen durchgeführt. Dies erfolgt am besten in einem eindimensionalen Farbraum. 

## Lösungsvorgehen
OpenCV stellt die Funktion `cv2.cvtColor()` zur Umwandlung von Bildern zur Verfügung.
Als Übergabeparameter wird die geforderte Farbkonvention angegeben.
- `cv2.COLOR_BGR2RGB`
- `cv2.COLOR_BGR2HSV`
- `cv2.COLOR_BGR2GRAY`
- `cv2....`

<img src="img/gray_scale.png" width="100%">
