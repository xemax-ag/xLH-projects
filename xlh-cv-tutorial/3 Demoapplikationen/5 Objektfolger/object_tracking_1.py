# object_tracking_1.py
import cv2
import numpy as np

bgr = np.array([[[129, 246, 225]]], dtype='uint8')
# Konvertierung in den HSV Farbraum
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
print(bgr, hsv)