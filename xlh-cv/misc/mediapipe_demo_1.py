# https://pypi.org/project/mediapipe/  =>  pip install mediapipe
# https://www.youtube.com/watch?v=v-ebX04SNYM
# https://github.com/google/mediapipe
# https://www.youtube.com/watch?v=vQZ4IvB07ec
# https://github.com/nicknochnack/MediaPipeHandPose/blob/main/Handpose%20Tutorial.ipynb
# https://arkalsekar.medium.com/how-to-get-all-the-co-ordinates-of-hand-using-mediapipe-hand-solutions-ac7e2742f702

import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

camera_nr = 0   # 0 = default, 1,2,3 = extra webcam
cap = cv2.VideoCapture(camera_nr, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap = cv2.VideoCapture(camera_nr)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip on horizontal
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Detections
        # print(results)

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )

                # x_coordinates = [landmark.x for landmark in hand]
                # y_coordinates = [landmark.y for landmark in hand]
                # print(x_coordinates, y_coordinates)

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()