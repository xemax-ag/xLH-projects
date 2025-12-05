# https://abhitronix.github.io/vidgear/v0.3.2-stable/switch_from_cv/
# https://abhitronix.github.io/vidgear/v0.3.2-stable/gears/#a-videocapture-gears

# import required libraries
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2

# Open suitable video stream, such as webcam on first index(i.e. 0)
stream = CamGear(source='rtsp://192.168.1.21:8554/cam').start()

# Define WriteGear Object with suitable output filename for e.g. `Output.mp4`
writer = WriteGear(output='Output.mp4')

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if None-type
    if frame is None:
        break


    # {do something with the frame here}


    # write frame to writer
    writer.write(frame)

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

# safely close writer
writer.close()