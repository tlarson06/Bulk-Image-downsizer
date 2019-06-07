# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:48:47 2019

@author: tlars
"""

from skimage import io, color, data, restoration
from PIL import Image
import imageio
import os
from os import listdir
from os.path import isfile, join
from tkinter.filedialog import askdirectory

data_dir = askdirectory()
data_dir_out = data_dir + '/downsized'

os.mkdir(data_dir_out)
onlyfiles = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

onlyjpg = [f for f in onlyfiles if f.lower().endswith('.jpg')]

size = 2250,1500

for x in onlyjpg:
    temp_img = Image.open(join(data_dir,x))
    temp_img = temp_img.resize(size,resample=Image.ANTIALIAS)
    temp_name = join(data_dir_out,os.path.splitext(x)[0])+'_small.jpg'
    temp_img.save(temp_name,"JPEG",quality=95)
