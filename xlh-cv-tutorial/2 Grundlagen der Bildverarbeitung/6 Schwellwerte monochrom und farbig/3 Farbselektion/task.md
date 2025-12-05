# Farbselektion
=> siehe auch Lektion Farbräume 

Weiter Informationen sind dem OpenCV Tutorial zu entnehmen:  
[OpenCv Python Tutorials: Changing Colorspaces](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html)

````python
# transformiere das Bild in den HSV Bereich
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# (h_min, s_min, v_min)
# (h_max, s_max, v_max)
threshold_color = cv2.inRange(image_hsv,
                              (15, 100,  50),
                              (45, 255, 255))
````

## Bestimmung der HSV Werte aus einem RGB Wert
Oft sind die RGB Werte einer Farbe bekannt. Der folgende Code zeigt eine exemplarische Umwandlung von RGB Werten in
den entpsrechenden HSV Wert auf:

````python
import cv2
import numpy as np

bgr = np.array([[[74, 158, 85]]], dtype='uint8')
# Konvertierung in den HSV Farbraum
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
print(bgr, hsv)

>>> [[[ 74 158  85]]] [[[ 56 136 158]]]
````

## ColorPix.exe
Hilfsmittel zur Bestimmung der Farbwerte eines Pixels.  
Das Programm ist hinterlegt im Ordner: `..\Videos\Videos\video\ColorPix\ColorPix.exe`
<img src="/img/color_pix.png">