# Schwellwerte
Unter Schwellwertbetrachtung wird die Binärisierung eines Bildes verstanden. 
Dabei wird ein Graustufenbild in die Werte 0 und 255 transformiert.
Das einfachste Beispiel besteht darin, einen Schwellwert T zu definieren, welcher das 
Bild in die zwei Elemente 0 un d 255 unterteilt.

```python
tresh_val = 190

# Bei einem Grauwert des Pixels > tresh_val wird das Pixel auf Weiss gesetzt.
(T, threshold) = cv2.threshold(blurred, tresh_val, 255, cv2.THRESH_BINARY)

# Bei einem Grauwert des Pixels > tresh_val wird das Pixel Schwarz gesetzt.
(T, threshold_inv) = cv2.threshold(blurred, tresh_val, 255, cv2.THRESH_BINARY_INV)
```