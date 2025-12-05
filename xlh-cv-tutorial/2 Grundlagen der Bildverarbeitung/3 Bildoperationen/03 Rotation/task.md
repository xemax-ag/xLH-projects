# Rotation
Die Rotation ist die Funktion der Drehung um einen Punkt P mit einem Winkel phi.

## Rotation im Bildzentrum
Falls der Drehpunkt im Zentrum des Bildes verankert ist, sieht die Rotationsmatrix 
folgendermassen aus:
<img src="/img/matrix_rotation_1.gif">

```python
# rotate_1.py
# Rotation um -30 Grad (Uhrzeigersinn) im Bildzentrum
rotated = imutils.rotate(image, -30)
```

## Rotation ausserhalb des Bildzentrums
Bei einem Drehpunkt ausserhalb des Zentrums ist die Rotationsmatrix um die Verschiebung 
zu erweitern.

```python
# rotate_2.py
# Rotation um -30 Grad (Uhrzeigersinn) im Punkt (0, 0) mit der Skalierung 0.5
rotated = imutils.rotate(image, -30, (0, 0), 0.5)
```
