# https://abhitronix.github.io/vidgear/v0.3.2-stable/gears/stabilizer/usage/

# import required libraries
from vidgear.gears.stabilizer import Stabilizer
import cv2

# Open suitable video stream, such as webcam on first index(i.e. 0)
stream = cv2.VideoCapture('rtsp://192.168.1.151:8554/cam')

# initiate stabilizer object with default parameters
stab = Stabilizer()

# loop over
while True:

    # read frames from stream
    (grabbed, frame) = stream.read()

    # check for frame if not grabbed
    if not grabbed:
        break

    # send current frame to stabilizer for processing
    stabilized_frame = stab.stabilize(frame)

    # wait for stabilizer which still be initializing
    if stabilized_frame is None:
        continue

    # {do something with the stabilized frame here}

    # Show output window
    cv2.imshow("Stabilized Frame", stabilized_frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# clear stabilizer resources
stab.clean()

# safely close video stream
stream.release()