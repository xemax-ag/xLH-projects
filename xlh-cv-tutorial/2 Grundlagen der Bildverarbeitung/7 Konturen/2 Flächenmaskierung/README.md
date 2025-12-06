# Flächenmaskierung
Die Flächenmaskierung erfolgt grundsätzlich im gleichen Stil wie die Erfassung der Konturen.
Der Unterschied besteht aus:
1. Der 3. Parameter in `cv2.drawContours` wird auf -1 gesetzt. Damit werden die Konturen als Fläche in die Maske 
   eingetragen.
2. Logische Operation zwischen der Leinwand und der Flächenmaske
 