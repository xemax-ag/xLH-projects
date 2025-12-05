# arithmetic.py
import cv2
import numpy as np
import imutils

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/box_with_bullets.png')

# Bilder sind NumPy Arrays vom Datentyp uint8.
# Bei der Verwendung der OpenCv Operationen, werden die Grenzen berücksichtigt.
print(f'Begrenzung auf max of 255: {cv2.add(np.uint8([180]), np.uint8([120]))}')
print(f'Begrenzung auf min of 0: {cv2.subtract(np.uint8([75]), np.uint8([125]))}')
# >>> Begrenzung auf max of 255: [[255]]
# >>> Begrenzung auf min of 0: [[0]]

# Bei der Benutzung der NumPy Operationen, werden die Grenzen modularisiert.
print(f'NumPy Addition: {np.uint8([200]) + np.uint8([100])}')
print(f'NumPy Subtraktion: {np.uint8([100]) - np.uint8([120])}')
# >>> NumPy Addition: [44]
# >>> NumPy Subtraktion: [236]

# Arithmetik auf das Bild angewendet
M = np.ones(image.shape, dtype="uint8") * 150
added = cv2.add(image, M)

# Zusammenfassung der Ausganslage und der Bearbeitung
result = np.hstack([image, added])

# schreibe das Bild in eine Datei
cv2.imwrite('img/arithmetic.png', result[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', result)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
