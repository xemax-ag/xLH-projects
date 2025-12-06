# Bildarithmetik
Bilder werden in OpenCV als NumPy Arrays vom Datentyp `uint8` behandelt. 

Somit lassen sich die gewohnten NumPy Operationen auf das Bildarray anwenden.

Wichtig: Bilder werden in der Form von vorzeichenlosen 8 Bit Integern dargestellt. 
Wird der Überlauf (0< und >255) nicht beachtet, entstehen Verfälschungen in der Bilddarstellung.
Deshalb wird empfohlen, anstelle der NumPy Operationen die OpenCV Funktionen zu verwenden.

```python
cv2.add(np.uint8([180]), np.uint8([120]))
cv2.subtract(np.uint8([75]), np.uint8([125]))
```

Die Multiplikation wird in der Lektion der Kernelfunktionen aufgezeigt.