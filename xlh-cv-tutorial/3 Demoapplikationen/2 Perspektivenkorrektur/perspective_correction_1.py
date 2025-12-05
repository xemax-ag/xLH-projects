import cv2
import imutils

GREEN = (0, 255, 0)


# Eventauswertung k
def cv2_imshow_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


# lade das Bild in ein NumPy Array
image = cv2.imread('img/perspecitve_red.jpg')
image = imutils.resize(image, width=800)

radius = 5
top_left = (241, 34)
top_right = (665, 27)
bottom_right = (754, 398)
bottom_left = (173, 402)
cv2.circle(image, top_left, radius, GREEN, -1)
cv2.circle(image, top_right, radius, GREEN, -1)
cv2.circle(image, bottom_right, radius, GREEN, -1)
cv2.circle(image, bottom_left, radius, GREEN, -1)

# zeige das Bild und warte auf einen Tastendruck
cv2.namedWindow('image')
cv2.setMouseCallback('image', cv2_imshow_event)
cv2.imshow('image', image)
cv2.moveWindow('image', 0, 0)
cv2.waitKey(0)

