# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:56:19 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np
import myMorphology
kernel = np.array([\
        [0, 1, 1, 1, 0], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [1, 1, 1, 1, 1], \
        [0, 1, 1, 1, 0]])

if __name__ == '__main__':
    lena = Image.open("lena.bmp")
    #binarization
    binary_lena = lena.point(lambda x: 0 if x < 128 else 255, '1')

    #HW4.1'
    dilation_lena = myMorphology.dilation(binary_lena, kernel)
    dilation_lena.save('dilation_lena.bmp')

    #HW4.2'
    erosion_lena = myMorphology.erosion(binary_lena, kernel)
    erosion_lena.save('erosion_lena.bmp')
