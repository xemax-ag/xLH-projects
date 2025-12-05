# cut_and_write.py
import cv2
from fps import Fps
import imutils
import numpy as np

# capture video stream from file
cap = cv2.VideoCapture('../../../Videos/Videos/video/Dubai_4k_2160p_60fps.webm')

# get the camera resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
print(frame_width, frame_height)

# define the fps for the output video
fps_out = cap.get(cv2.CAP_PROP_FPS)
print('fps_out', fps_out)

# define the codec and create VideoWriter object
# information about 4 letters codecs:
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#saving-a-video
out_fhd = cv2.VideoWriter('video/output_fhd.mp4v', cv2.VideoWriter_fourcc(*'XVID'),
                          fps_out, (960, 540))

out_cut = cv2.VideoWriter('video/output_cut.mp4v', cv2.VideoWriter_fourcc(*'XVID'),
                          fps_out, (600, 400))

fps = Fps()

n = 0
while(True):
    if cap.isOpened():
        # capture
        ret, frame = cap.read()
        fps.update()
        if ret:
            frame_cut = frame[1500:1900, 1050:1650]
            #print(np.shape(frame_cut))
            frame = imutils.resize(frame, width=960)

            cv2.imshow('frame', frame)
            cv2.moveWindow('frame', 0, 0)

            cv2.imshow('frame_cut', frame_cut)
            cv2.moveWindow('frame_cut', 0, 600)

            # write the frame into the file
            out_fhd.write(frame)
            out_cut.write(frame_cut)
            n += 1

    if n > 90:  # die ersten 3 Sekunden bei einer Framerate von 30 Bildern pro Sekunde
        break

    cv2_key = cv2.waitKey(1) & 0xFF
    if cv2_key == ord('q'):
        break
    elif cv2_key == ord('s'):
        print('save frame as png')
        cv2.imwrite("img/frame.png", frame)
    elif cv2_key == ord('f'):
        print(f'fps: {fps.fps:1.1f}')

# when everything done, release the capture
cap.release()
out_fhd.release()
cv2.destroyAllWindows()
print('done')
