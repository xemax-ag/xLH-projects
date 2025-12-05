# Farbräume
Der Farbraum ist eine Beschreibungsform welche es erlaubt eine konsistente 
Beschreibung der Farbe zu definieren.

# RGB Farbraum
Im Bereiche der Computertechnik wird oft der RGB Farbraum verwendet.
Die einzelnen Farbanteile Rot, Blau und Grün bewegen sich in einem Bereich zwischen 0-255.
Durch additive Farbmischung sind bis zu 256 x 256 x 256 = 16'777'216 Farben unterscheidbar.
<img src="/img/rgb_cube.jpg" width="50%">

# HSV Farbraum
Der HSV Farbraum transformiert den RGB Farbraum in einen Zylinder.  
Die einzelnen Komponenten sind:
* Hue: Farbwert in einem Bereich 0-360 (Hinweis: In OpenCV werden Farben als uInt8 dargestellt. Dies führt dazu,
  dass der Hue-Wert in den Bereich 0-179 skaliert wird.)
*  Saturation: Weissanteil der Farbe in einem Bereich 0-255.
* Value: Helligkeit des Farbwertes in einem Bereich 0-255.

<img src="img/hsv_colorspace.jpg" width="50%">
.
<img src="img/hsv_color_wheel.jpg" width="50%">

## Lab Farbraum
Der Lab Farbraum beschreibt alle wahrnembaren Farben.
Er nutzt einen dreidimensionalen Farbenraum, bei dem der Helligkeitswert L* senkrecht auf der Farbebene (a*,b*) steht.

<img src="/img/lab_color_space.jpg" width="50%">


## Weitere Information
* [Wikipedia: RGB-Farbraum](https://de.wikipedia.org/wiki/RGB-Farbraum)
* [Wikipedia: HSV-Farbraum](https://de.wikipedia.org/wiki/HSV-Farbraum)
* [Wikipedia: Lab-Farbraum](https://de.wikipedia.org/wiki/Lab-Farbraum)
  
  