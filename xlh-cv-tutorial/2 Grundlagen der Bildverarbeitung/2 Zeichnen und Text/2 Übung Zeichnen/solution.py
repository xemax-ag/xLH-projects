import cv2

# Farbdefintionen
RED = (0, 0, 255)

# lade Bild von der Datei in ein NumPy Array
image = cv2.imread('img/python_snake.jpg')

# zeichne einen Kreis um die beiden Augen
cv2.circle(image, (205, 605), 30, RED, 10)
cv2.circle(image, (345, 640), 35, RED, 10)

# schreibe das Bild in eine Datei
cv2.imwrite('img/solution.png', image[0:-2, 0:-2])

# Anzeige auf dem Bildschirm
cv2.imshow('Ausgabe', image)
cv2.moveWindow('Ausgabe', 100, 100)
cv2.waitKey(0)
