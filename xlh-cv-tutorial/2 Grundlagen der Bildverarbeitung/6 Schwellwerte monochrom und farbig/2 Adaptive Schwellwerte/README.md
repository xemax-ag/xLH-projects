# Adaptive Schwellwerte
Die adaptive Schwellwertbetrachtung sucht automatischen einen optimalen Wert für
den Schwellwert T.  

Weitere Informationen sind der Modulbeschreibung unter `threshold_local` zu entnehmen:
[scikit-image: image filters](https://scikit-image.org/docs/dev/api/skimage.filters.html)


````python
from skimage.filters import threshold_local
...
T = threshold_local(blurred, 51, offset=0.10, method="gaussian")
threshold = (blurred >= T).astype("uint8") * 255
threshold_inv = (blurred < T).astype("uint8") * 255
````