# https://abhitronix.github.io/vidgear/v0.3.2-stable/gears/videogear/usage/#using-videogear-with-video-stabilizer-backend
"""
QVGA: 320 × 240
VGA: 640 × 480
WQVGA: 432 × 240
WVGA: 720 × 400, 800 × 480, 848 × 480, 852 × 480, 864 × 480 oder 858 × 484
DVGA: 960 × 640
WSVGA: 1024 × 600, 1072 × 600
"""


# import required libraries
from vidgear.gears import VideoGear
import cv2


# define suitable tweak parameters for your stream.
options = {
    # "CAP_PROP_FRAME_WIDTH": 800,
    # "CAP_PROP_FRAME_HEIGHT": 480,
    "CAP_PROP_FPS": 50,
}

# To open live video stream on webcam at first index(i.e. 0)
# device and apply source tweak parameters
# stream = VideoGear(source='rtsp://192.168.1.151:8554/cam', logging=True, **options).start()
stream = VideoGear(source='rtsp://192.168.1.142:8554/cam',
                   stabilize=False,
                   logging=True,
                   **options).start()

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()
