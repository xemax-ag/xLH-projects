# https://arkalsekar.medium.com/how-to-get-all-the-co-ordinates-of-hand-using-mediapipe-hand-solutions-ac7e2742f702
# https://toptechboy.com/distinguish-between-right-and-left-hands-in-mediapipe/

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

camera_nr = 0   # 0 = default, 1,2,3 = extra webcam
# cap = cv2.VideoCapture(camera_nr, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap = cv2.VideoCapture(camera_nr)

with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    image_height, image_width, _ = image.shape
    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      cx4 = -1
      cy4 = -1
      cx8 = -1
      cy8 = -1
      for hand_landmarks in results.multi_hand_landmarks:
        # Here is How to Get All the Coordinates
        for ids, landmrk in enumerate(hand_landmarks.landmark):
            # print(ids, landmrk)
            cx, cy = landmrk.x * image_width, landmrk.y*image_height
            if ids == 4:
              # print(ids, cx, cy)
              cx4 = cx
              cy4 = cy
            if ids == 4:
              # print(ids, cx, cy)
              cx8 = cx
              cy8 = cy
              # print (ids, cx, cy)

        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
      print('============================================================')

    cv2.imshow('MediaPipe Hands', image)
    # if cv2.waitKey(5) & 0xFF == 27:
    #   break
cap.release()
cv2.destroyAllWindows()