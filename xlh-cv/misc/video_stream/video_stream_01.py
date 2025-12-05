# https://abhitronix.github.io/vidgear/v0.3.2-stable/switch_from_cv/
# https://abhitronix.github.io/vidgear/v0.3.2-stable/gears/#a-videocapture-gears

# import required libraries
from vidgear.gears import CamGear
import cv2

# Open suitable video stream, such as webcam on first index(i.e. 0)
# stream = CamGear(source='rtsp://192.168.1.151:8554/cam').start()
stream = CamGear(source='rtsp://192.168.31.31:8554/cam').start()
# stream = CamGear(source='output.mp4').start()

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