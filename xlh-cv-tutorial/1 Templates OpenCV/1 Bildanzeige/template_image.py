# template_image.py
import cv2

# load the image and show some basic information on it
image = cv2.imread('image.png')
print(f'width: {image.shape[1]} pixels')
print(f'height: {image.shape[0]}  pixels')
print(f'channels: {image.shape[2]}')
print(f'bgr value of a pixel: {image[150][600]}')

# show the image and wait for a keypress
cv2.imshow('image_window', image)
cv2.moveWindow('image_window', 0, 0)
cv2.waitKey(0)

# save the image (opencv detects automaticaly the imagetype)1
cv2.imwrite("image_png.png", image)
cv2.imwrite("image_jpg.jpg", image)
