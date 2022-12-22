# coding:utf-8

from PIL import Image

image = Image.open('creator.jpg')
image.format = 'PNG'
image.mode = 'RGB'
image.crop((80, 20, 310, 360)).show()
