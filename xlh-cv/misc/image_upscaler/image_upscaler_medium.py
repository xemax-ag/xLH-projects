# https://medium.com/django-unleashed/ai-image-upscale-made-easy-no-gpu-needed-ea9195f39647

import torch
from PIL import Image
from RealESRGAN import RealESRGAN
import requests

# Device CPU
device = torch.device('cuda')

# Load model and scale factor
model = RealESRGAN(device, scale=4)
model.load_weights('weights/RealESRGAN_x4.pth', download=True)

# Load image
path_to_image = 'image_in.jpg'
image = Image.open(path_to_image).convert('RGB')
# url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
# url = 'https://cdn.pixabay.com/photo/2017/02/07/16/47/kingfisher-2046453_640.jpg'
# image = Image.open(requests.get(url, stream=True).raw)
# path_to_image = 'T_Bot_Controller.png'


# Upscale image
sr_image = model.predict(image)

# Save image
sr_image.save('image_out.jpg')