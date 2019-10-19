# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:56:19 2019

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
    # binarization
    binary_lena = lena.point(lambda x: 0 if x < 128 else 255, '1')

    # HW4(a)
    dilation_lena = myMorphology.dilation(binary_lena, kernel, centerKernel)
    dilation_lena.save('dilation_lena.bmp')

    # HW4(b)
    erosion_lena = myMorphology.erosion(binary_lena, kernel, centerKernel)
    erosion_lena.save('erosion_lena.bmp')

    # HW4(c)
    opening_lena = myMorphology.opening(binary_lena, kernel, centerKernel)
    opening_lena.save('opening_lena.bmp')

    # HW4(d)
    closing_lena = myMorphology.closing(binary_lena, kernel, centerKernel)
    closing_lena.save('closing_lena.bmp')

    # HW4(e)
    kernel_J = np.array([
        [1, 1],
        [0, 1]])
    centerKernel_J = (1, 0)
    kernel_K = np.array([
        [1, 1],
        [0, 1]])
    centerKernel_K = (0, 1)
    hitmiss_lena = myMorphology.hitmiss(binary_lena,
                                       kernel_J, centerKernel_J,
                                       kernel_K, centerKernel_K)
    # Save image fo file.
    hitmiss_lena.save('hitmiss_lena.bmp')
