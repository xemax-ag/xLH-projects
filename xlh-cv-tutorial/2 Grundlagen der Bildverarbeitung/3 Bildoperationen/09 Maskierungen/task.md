# Maskierungen 
Mithilfe der Maskierungen besteht die Möglichkeit, Bereiche in Farbbildern zu extrahieren bzw. zu
verbergen. Die bitweisen Funktionen werden mit dem Parameter mask aufgerufen.

```python
masked = cv2.bitwise_and(image, image, mask=mask)
```

Dabei ist zu zu beachten, dass die Maske die gleichen Abmasse in Breite und Höhe 
wie das Vergleichsbild aufweisen muss.