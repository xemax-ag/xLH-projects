# template_webcam_writer.py
import cv2
from fps import Fps

# capture video stream from webcam
camera_nr = 0  # 0 = default, 1,2,3 = extra webcam
cap = cv2.VideoCapture(camera_nr, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# check if camera opened successfully
if not cap.isOpened():
    print("unable to read camera feed")

# get the camera resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print(frame_width, frame_height)

# define the fps for the output video
fps_out = 16

# define the codec and create VideoWriter object
# information about 4 letters codecs:
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#saving-a-video
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID'),
                      fps_out, (frame_width, frame_height))

fps = Fps()

while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        fps.update()
        if ret:
            cv2.imshow('frame', frame)
            cv2.moveWindow('frame', 0, 0)

            # write the frame into the output file
            out.write(frame)

    cv2_key = cv2.waitKey(1) & 0xFF
    if cv2_key == ord('q'):
        break
    elif cv2_key == ord('s'):
        print('save frame as png')
        cv2.imwrite("frame.png", frame)
    elif cv2_key == ord('f'):
        print(f'fps: {fps.fps:1.1f}')

# when everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()

