# background_subtraction_4.py
import cv2


class BackgroundSubtraction:
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)

    def __init__(self):
        # Hintergrundsubtraktion
        self.back_sub = cv2.createBackgroundSubtractorMOG2()
        self.back_sub.setDetectShadows(True)
        self.back_sub.setShadowValue(0)
        self.back_sub.setHistory(1000)
        self.min_area = 3000

    def apply_sub(self, src):
        # Maskierung der Bilddifferenz
        fgMask = self.back_sub.apply(src, learningRate=0.01)
        # entferne Pixelrauschen
        eroded = cv2.erode(fgMask, None, iterations=2)
        # verbinden von weissen Einzelpunkten
        dilated = cv2.dilate(eroded, None, iterations=20)
        # Maskierung der bewegten Bildelement aus dem Ursprungsframe
        masked = cv2.bitwise_and(src, src, mask=dilated)
        # finde alle äusseren Konturen und markiere diese im Bild
        masked_gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
        cnts, hir = cv2.findContours(masked_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        conturs = src.copy()
        cv2.drawContours(conturs, cnts, -1, BackgroundSubtraction.GREEN, 2)
        # loop over the contours again
        center_of_mass = masked.copy()
        for (i, c) in enumerate(cnts):
            # compute the area and the perimeter of the contour
            area = cv2.contourArea(c)
            if area > self.min_area:
                # draw the contour on the image
                cv2.drawContours(center_of_mass, [c], -1, BackgroundSubtraction.GREEN, 2)
                # compute the center of the contour and draw the contour number
                M = cv2.moments(c)
                cX = int(M['m10'] / M['m00'])
                cY = int(M['m01'] / M['m00'])
                cv2.circle(center_of_mass, (cX, cY), 5, BackgroundSubtraction.RED, -1)

        return center_of_mass
