# green_screen_step_1.py
import cv2
import numpy as np

bgr = np.array([[[74, 158, 85]]], dtype='uint8')
# Konvertierung in den HSV Farbraum
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
print(bgr, hsv)