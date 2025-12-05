import cv2
import imutils
import numpy as np

GREEN = (0, 255, 0)


# Eventauswertung
def cv2_imshow_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


def four_point_transform(image, tl, tr, br, bl):
    # berechne die Breite
    width_a = np.sqrt(((br[0] - bl[0])**2) + ((br[1] - bl[1])**2))
    width_b = np.sqrt(((tr[0] - tl[0])**2) + ((tr[1] - tl[1])**2))
    max_width = max(int(width_a), int(width_b))

    # berechne die Höhe
    height_a = np.sqrt(((tr[0] - br[0])**2) + ((tr[1] - br[1])**2))
    height_b = np.sqrt(((tl[0] - bl[0])**2) + ((tl[1] - bl[1])**2))
    max_height = max(int(height_a), int(height_b))

    # definiere die Zielpunkte des transformierten Bildes
    destination_ponints = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype="float32")

    # Umwandlung der Ausgangspunkte in der Form eines NumPy Arrays
    rect = np.zeros((4, 2), dtype="float32")
    rect[0] = tl; rect[1] = tr; rect[2] = br; rect[3] = bl

    # berechne die Transformationsmatrix
    transformation_matrix = cv2.getPerspectiveTransform(rect, destination_ponints)
    warped = cv2.warpPerspective(image, transformation_matrix, (max_width, max_height))
    return warped


# lade das Bild in ein NumPy Array
image = cv2.imread('img/perspecitve_red.jpg')
image = imutils.resize(image, width=800)

top_left = (241, 36)
top_right = (665, 27)
bottom_right = (753, 397)
bottom_left = (173, 402)

# das Bild wird begradigt
transformation = four_point_transform(image, top_left, top_right, bottom_right, bottom_left)
# das Ursprungsbild stellt ein Quadrat dar, somit ist ein weiterer Schritt notwendig
print(np.shape(transformation))
min_len = min(np.shape(transformation)[0], np.shape(transformation)[1])
transformation_square = cv2.resize(transformation, (min_len, min_len), interpolation=cv2.INTER_AREA)

# Berechnung der Auflösung / Pixel
nr_of_pixels = np.shape(transformation_square)[0]
grid_width_mm = 170
resolution_per_pixel = grid_width_mm / nr_of_pixels
print(nr_of_pixels, grid_width_mm, resolution_per_pixel)

# zeichne die Eckpunkte in das Bild ein
radius = 5
cv2.circle(image, top_left, radius, GREEN, -1)
cv2.circle(image, top_right, radius, GREEN, -1)
cv2.circle(image, bottom_right, radius, GREEN, -1)
cv2.circle(image, bottom_left, radius, GREEN, -1)

# zeige das Bild und warte auf einen Tastendruck
cv2.namedWindow('image')
cv2.setMouseCallback('image', cv2_imshow_event)
cv2.imshow('image', image)
cv2.moveWindow('image', 100, 100)
cv2.imshow('transformation', transformation)
cv2.moveWindow('transformation', 100, 600)
cv2.imshow('transformation_square', transformation_square)
cv2.moveWindow('transformation_square', 700, 600)

cv2.waitKey(0)

