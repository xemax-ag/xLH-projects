# https://pypi.org/project/super-image/

from super_image import EdsrModel, ImageLoader
from PIL import Image
import requests

url = 'https://paperswithcode.com/media/datasets/Set5-0000002728-07a9793f_zA3bDjj.jpg'
url = 'https://cdn.pixabay.com/photo/2017/02/07/16/47/kingfisher-2046453_640.jpg'
image = Image.open(requests.get(url, stream=True).raw)

model = EdsrModel.from_pretrained('eugenesiow/edsr', scale=3)
inputs = ImageLoader.load_image(image)
preds = model(inputs)

ImageLoader.save_image(preds, 'scaled_4x.png')
ImageLoader.save_compare(inputs, preds, 'scaled_4x_compare.png')