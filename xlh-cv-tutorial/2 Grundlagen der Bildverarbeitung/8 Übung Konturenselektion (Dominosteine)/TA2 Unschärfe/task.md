# TA2 Unschärfe (Blur)

## Aufgabe
Das Graustufenbild ist zu glätten.

## Hintergrundinformationen
Damit Bildstörungen nicht fälschlicherweise als Kontur registriert werden, ist es empfehlenswert
das Bild zu glätten. In der Signalverarbeitung entspricht die Bildglättung dem Filtern. 
Mit dem Blur-Algorithmus wird eine gewichtete Mittelwertbildung eines Pixels durchgeführt.
In der Funktion `cv2.GaussianBlur(canvas, kernel_size, 0)` ist die Kernelgrösse zu definieren. Der
Kernel muss stehts als Tupel mit ungeradzahligen Pixelzahlen in x- und y-Richtung angegeben werden.
Die Begründung liefert die Website [https://setosa.io/ev/image-kernels/](https://setosa.io/ev/image-kernels/).
<img src="img/setosa_io.png" width="100%"> 

## Lösungsvorgehen
OpenCV stellt die Funktion `cv2.GaussianBlur()` zur Erstellung einer Gausschen Unschärfe von Bildern zur Verfügung.
<img src="img/blur.png" width="100%">
