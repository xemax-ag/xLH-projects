# Zeichnen 1

## Leinwand
Da eine Leinwand einem 3-dimensonalen NumPy Array entsricht, erfolgt die Erstellung dementsprechend
über die bereits bekannten NumPy Operationen.<br>
Im Code werden die zwei Möglichkeiten exemplarisch aufgezeigt.

## Linie cv2.line
cv2.line(leinwand, (x_start, y_start), (x_ende, y_ende), farbe, dicke)

Farben sind als Tupel in der BGR Reihenfolge anzugeben:
* BLACK = (0, 0, 0)
* WHITE = (255, 255, 255)
* RED = (0, 0, 255)
* GREEN = (0, 255, 0)
* BLUE = (255, 0, 0)

## Rechteck
cv2.rectangle(leinwand, (x_start, y_start), (x_ende, y_ende), farbe, dicke)

* Dicke >= 1 entspricht der Strichdicke des Rahmens
* Dicke == -1 führt zu einem ausgefüllten Rechteck

## Kreis
cv2.circle(leinwand, (x_zentrum, y_zentrum), radius, farbe, dicke)

* Dicke >= 1 entspricht der Strichdicke der Kreislinie
* Dicke == -1 führt zu einem ausgefüllten Kreis

## Elipse
cv2.ellipse(leinwand, (x_zentrum, y_zentrum), (x_achse, y_achse), neigung, winkel_start, winkel_ende, farbe, dicke)

* Dicke >= 1 entspricht der Strichdicke der Elipsenlinie
* Dicke == -1 führt zu einer ausgefüllten Elipse
