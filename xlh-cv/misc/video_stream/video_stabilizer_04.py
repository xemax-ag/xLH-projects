# https://abhitronix.github.io/vidgear/v0.3.2-stable/gears/stabilizer/usage/

# import required libraries
from vidgear.gears.stabilizer import Stabilizer
from vidgear.gears import CamGear
from vidgear.gears import VideoGear
import cv2

# To open live video stream on webcam at first index(i.e. 0) device
# stream = CamGear(source=0).start()

# define suitable tweak parameters for your stream.
options = {
    "CAP_PROP_FRAME_WIDTH": 320, # resolution 320x240
    "CAP_PROP_FRAME_HEIGHT": 240,
    "CAP_PROP_FPS": 10, # framerate 60fps
}

# To open live video stream on webcam at first index(i.e. 0)
# device and apply source tweak parameters
# stream = VideoGear(source='rtsp://192.168.1.151:8554/cam', logging=True, **options).start()
stream = VideoGear(source='rtsp://192.168.31.31:8554/cam', logging=True, **options).start()

# initiate stabilizer object with default parameters
stab = Stabilizer()

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # send current frame to stabilizer for processing
    stabilized_frame = stab.stabilize(frame)

    # wait for stabilizer which still be initializing
    if stabilized_frame is None:
        continue

    # {do something with the stabilized frame here}

    # Show output window
    cv2.imshow("Output Stabilized Frame", stabilized_frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# clear stabilizer resources
stab.clean()

# safely close video stream
stream.stop()