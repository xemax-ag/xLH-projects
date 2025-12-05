import cv2
import numpy as np
from skimage.filters import threshold_local

# definiere den Font und die Farbe
font = cv2.FONT_HERSHEY_SIMPLEX
WHITE = 255
RED = (0, 0, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/domino_1.jpg')[4:-4, 4:-4]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blurfilter
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Bei einem Pixelwert > 100 wird das Pixel auf Weiss gesetzt.
(T, threshold) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

# adaptive Schwellwertbetrachtung
T = threshold_local(blurred, 199, offset=0, method="gaussian")
threshold_adaptive = (blurred >= T).astype("uint8") * 255

# Morphologische Operationen
eroded = cv2.erode(threshold, None, iterations=2)
dilated = cv2.dilate(eroded, None, iterations=2)

# Zusammenfassung der Ausganslage und der Bearbeitung
image = cv2.putText(image, 'Original', (25, 25), font, 0.8, RED, 2, cv2.LINE_AA)
gray = cv2.putText(gray, 'Graustufenbild', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
blurred = cv2.putText(blurred, 'Unschaerfe', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
threshold = cv2.putText(threshold, 'Schwellwert', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
threshold_adaptive = cv2.putText(threshold_adaptive, 'adaptiver Schwellwert', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
eroded = cv2.putText(eroded, 'Reduzierung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)
dilated = cv2.putText(dilated, 'Erweiterung', (25, 25), font, 0.8, WHITE, 2, cv2.LINE_AA)

result_1 = np.hstack([image])
result_2 = np.hstack([gray, blurred])
result_3 = np.hstack([threshold, threshold_adaptive])
result_4 = np.hstack([eroded, dilated])

result_stack_mono = np.vstack([result_2, result_3, result_4])

# schreibe das Bild in eine Datei
cv2.imwrite('img/morphological.png', result_stack_mono[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe_farbig', result_1)
cv2.moveWindow('Ausgabe_farbig', 100, 100)
cv2.imshow('Ausgabe_monochrom', result_stack_mono)
cv2.moveWindow('Ausgabe_monochrom', 100, 460)
cv2.waitKey(0)
