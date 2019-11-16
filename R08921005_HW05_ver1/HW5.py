# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:32:58 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np
import myMorphology
kernel = np.array([
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0]])
centerKernel = tuple([x // 2 for x in kernel.shape])

if __name__ == '__main__':
    lena = Image.open("lena.bmp")
    # HW5a)
    dilation_lena = myMorphology.dilation(lena, kernel, centerKernel)
    dilation_lena.save('dilation_lena.bmp')

    # HW5(b)
    erosion_lena = myMorphology.erosion(lena, kernel, centerKernel)
    erosion_lena.save('erosion_lena.bmp')

    # HW5(c)
    opening_lena = myMorphology.opening(lena, kernel, centerKernel)
    opening_lena.save('opening_lena.bmp')

    # HW5(d)
    closing_lena = myMorphology.closing(lena, kernel, centerKernel)
    closing_lena.save('closing_lena.bmp')
