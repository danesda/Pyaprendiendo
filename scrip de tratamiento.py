# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import skimage
from matplotlib import pyplot as plt
from IPython.display import Image

Image(filename='oy.jpg',height=400,width=500)

import skimage
from skimage import data
camera = data.camera()

from skimage import io
img = io.imread('oy.jpg')
io.imshow(img)
io.show()

print (img.shape)


Image(filename='nave.jpg',height=500,width=600)

from skimage import io
img = io.imread('nave.jpg')
io.imshow(img)
io.show()

from skimage import io,color #importar modulo color

img = io.imread("nave.jpg")
img_gris = color.rgb2gray(img)
io.imshow(img_gris)
io.show()

import matplotlib.pyplot as plt
from skimage import io,color

img = io.imread("nave.jpg")
img_gris = color.rgb2gray(img)
plt.subplot(211)
io.imshow(img)
plt.subplot(212)
io.imshow(img_gris)
io.show()

img=np.uint8(np.dot(img[...,:3],[.0,.0, 1]))

import matplotlib.pyplot as plt
from skimage import io,color


