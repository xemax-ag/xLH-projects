# https://abhitronix.github.io/vidgear/v0.3.2-stable/gears/videogear/usage/#using-videogear-with-video-stabilizer-backend
# https://abhitronix.github.io/vidgear/v0.3.2-stable/bonus/reference/stabilizer/

# import required libraries
from vidgear.gears import VideoGear
import numpy as np
import cv2

# define suitable tweak parameters for your stream.
options = {
    # "CAP_PROP_FRAME_WIDTH": 320, # resolution 320x240
    # "CAP_PROP_FRAME_HEIGHT": 240,
    "CAP_PROP_FPS": 50, # framerate 60fps
}

# open any valid video stream with stabilization enabled(`stabilize = True`)
# stream_stab = VideoGear(source='rtsp://192.168.1.151:8554/cam', **options, stabilize=True).start()
stream_stab = VideoGear(source='rtsp://192.168.31.31:8554/cam',
                        stabilize=True,
                        logging=True,
                        **options).start()

# loop over
while True:

    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if None-type
    if frame_stab is None:
        break

    # {do something with the frame here}

    # Show output window
    cv2.imshow("Stabilized Output", frame_stab)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close streams
stream_stab.stop()
