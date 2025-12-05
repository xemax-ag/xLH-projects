# Übung Konturenselektion (Dominosteine)

# Aufgabe
Im Bild `/img/domino_1.jpg` sind die Anzahl Punkte des Dominosteines auf der linken und rechten Seite mittels 
bildverarbeitenden Algorithmen zu bestimmen.
<img src="/img/domino_1.jpg" width="30%">

## Lösungsvorgehen
Ein mögliches Lösungsvorgehen kann sein:
1. Graustufenumwandlung
2. Unschärfe (Blur) auf das Graustufenbild anwenden
3. Schwellwertbetrachtung zur Selektion von Punkten und Trennstrich
4. Morphologische Operationen um das Pixelrauschen zu beseitigen
5. Konturenbetrachtung 
  - a. Betrachtung aller Konturen
  - b. Betrachtung der äusseren Konturen
  - c. Trennung von Punkt und Querstrich
6. Zählen der Punkte auf der linken und der rechten Seite

<img src="img/solution.png" width="100%">

## Lösungsvorgehen
Die Umsetzung der Aufgabenstellung kann in zwei möglichen Varianten erfolgen:
1. Sie lösen sämtliche Schritte der Aufgabenstellung in einem Schritt.
2. Sie folgen den Lösungsvorschlägen welche in den Teilaufgaben (TA) 1-6 erläutert werden.

## Erweiterungsmöglichkeiten
* Winkelbestimmung des Dominosteins mittels Bounding Boxen
* Farbfilter anwenden zur Unterscheidung der Farben
* Erweiterung des Algorithmus auf Bilder mit mehreren Dominosteinen
  * `/img/domino_2.jpg`
  * `/img/domino_3.jpg`

<img src="img/domino_2.jpg" width="25%">
.  
<img src="img/domino_3.jpg" width="25%">

