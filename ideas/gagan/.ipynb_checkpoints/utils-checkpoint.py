import numpy as np
from PIL import Image
import torch
from torchvision import models
import torchvision.transforms as T
import os

def get_image(path, crop = []):
    img = Image.open(path)
    img = img.rotate(90, expand = 1)
    return img.crop(crop)

def crop_grid(img, box_size = [900,500], top_offset = 0):
    # can you split the image into small boxes of this size ? 
    H,W = img.size
    nrows = int(np.floor(H / box_size[0]))
    ncols = int(np.floor(W / box_size[1]))
    imgs = []
    
    left = 0
    up = 0
    low = up + box_size[1]
    right = left + box_size[0]
    for i in range(nrows):
        for j in range(ncols):
            I = img.crop((left, up, right, low))
            imgs.append(I)
            left += box_size[0]
            right = left + box_size[0]
        up += box_size[1]
        low = up + box_size[1]
        left = 0
        right = left + box_size[0]
    return imgs

