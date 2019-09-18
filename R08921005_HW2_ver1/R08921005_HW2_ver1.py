# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:33:55 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np

lena_pic = Image.open( "lena.bmp" )
original_lena_array = np.array(lena_pic)
###########################################################
#(a)	a binary image (threshold at 128)
binarize_lena= original_lena_array.copy()
for ii in range(len(original_lena_array)):
    for jj in range(len(original_lena_array[ii])):
        if (original_lena_array[ii][jj]>=128):
            binarize_lena[ii][jj]=255
        else:
            binarize_lena[ii][jj]=0
Image.fromarray(binarize_lena.astype(np.uint8)).save('binarize_lena.bmp')