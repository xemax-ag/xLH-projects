# green_screen_step_5.py
import cv2
import imutils
import numpy as np


class GreenScreen:
    def __init__(self):
        self.hsv_min = (35, 50, 50)
        self.hsm_max = (75, 200, 255)
        self.blur_kernel = (15, 15)
        self.erode_iterations = 1
        self.dilate_iterations = 2

    def replace_green_screen(self, image_foreground, image_background):
        # Gaussian Blurfilter
        if self.blur_kernel[0] > 0:
            blurred = cv2.GaussianBlur(image_foreground, self.blur_kernel, 0)
        else:
            blurred = image_foreground

        # transformiere das Bild in den HSV Bereich
        image_hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # Schwellwertbetrachtung
        threshold_color = cv2.inRange(image_hsv, self.hsv_min, self.hsm_max)

        # Erodierung, Dilate
        if self.erode_iterations > 0:
            eroded = cv2.erode(threshold_color, None, iterations=self.erode_iterations)
        else:
            eroded = threshold_color

        if self.dilate_iterations > 0:
            dilated = cv2.dilate(eroded, None, iterations=self.dilate_iterations)
        else:
            dilated = eroded
        dilated_not = cv2.bitwise_not(dilated)

        # Die Maske muss in der gleichen Farbdimension des Bildes liegen.
        masked_image_invers = cv2.bitwise_and(image_foreground, image_foreground, mask=dilated_not)
        masked_background = cv2.bitwise_and(image_background, image_background, mask=dilated)

        # Addition der Maskierungen
        new_image = cv2.add(masked_background, masked_image_invers)
        return new_image


if __name__ == '__main__':
    # lade Bild von der Datei in ein NumPy Array
    image = cv2.imread('img/green_screen.png')
    image = imutils.resize(image, width=480)

    # lade Hintergrundbild von der Datei in ein NumPy Array
    background = cv2.imread('img/background.png')
    background = imutils.resize(background, width=480)

    # Instanzierung der Klasse
    green_screen = GreenScreen()
    new_image = green_screen.replace_green_screen(image, background)
    result = np.hstack([image, new_image])

    # Anzeige auf dem Bildschirm
    cv2.imshow('Ausgabe', result)
    cv2.moveWindow('Ausgabe', 100, 100)
    cv2.waitKey(0)
