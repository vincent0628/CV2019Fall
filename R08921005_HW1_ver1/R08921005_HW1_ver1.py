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
############             Part1                 ############ 
#part(a) upside-down lena.bmp
upside_down_lena= original_lena_array.copy()
for i in range(len(original_lena_array)):
    for j in range(len(original_lena_array[i])):
        upside_down_lena[len(original_lena_array)-i-1][j]=original_lena_array[i][j]
Image.fromarray(upside_down_lena.astype(np.uint8)).save('upside_down_lena.bmp')

#part(b) right-side-left lena.bmp
right_side_left_lena = original_lena_array.copy()
for i in range(len(original_lena_array)):
    for j in range(len(original_lena_array[i])):
        right_side_left_lena[i][len(original_lena_array)-j-1]=original_lena_array[i][j]
Image.fromarray(right_side_left_lena.astype(np.uint8)).save('right_side_left_lena.bmp')

#part(c)diagonally mirrored lena.bmp
diagonally_mirrored_lena = original_lena_array.copy()
for i in range(len(original_lena_array)):
    for j in range(len(original_lena_array[i])):
        diagonally_mirrored_lena[len(original_lena_array)-i-1][len(original_lena_array)-j-1]=original_lena_array[i][j]
Image.fromarray(diagonally_mirrored_lena.astype(np.uint8)).save('diagonally_mirrored_lena.bmp')
###########################################################
###########################################################
############             Part2                 ############ 
#part(d) rotate lena.bmp 45 degrees clockwise
from scipy import ndimage
rotate_lena = ndimage.rotate(original_lena_array, 45, reshape=True)
Image.fromarray(rotate_lena.astype(np.uint8)).save('rotate_lena.bmp')

#part(e) shrink lena.bmp in half
half = 0.5
shrink_lena = lena_pic.resize( [int(half * s) for s in lena_pic.size] )
shrink_lena.save('shrink_lena.bmp')

#(f) binarize lena.bmp at 128 to get a binary image
binarize_lena= original_lena_array.copy()
for i in range(len(original_lena_array)):
    for j in range(len(original_lena_array[i])):
        if (original_lena_array[i][j]>=128):
            binarize_lena[i][j]=255
        else:
            binarize_lena[i][j]=0
Image.fromarray(binarize_lena.astype(np.uint8)).save('binarize_lena.bmp')