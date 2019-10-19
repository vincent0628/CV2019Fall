# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:56:19 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np
def dilation(originalImage, kernel):
    """
    :type originalImage: Image 
    :type kernel: numpy array
    :return type: Image 
    """
    centerKernel = tuple([ x//2 for x in kernel.shape])
    dilationImage = Image.new('1', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            originalPixel = originalImage.getpixel((r, c))
            # If this pixel is 1 not white
            if(originalPixel!=0):
                for ii in range(kernel.shape[0]):
                    for jj in range(kernel.shape[1]):
                        if(kernel[ii,jj]):
                            targetX = r + (ii - centerKernel[0])
                            targetY = c + (jj - centerKernel[1])
                            if ((0<targetX<originalImage.size[0])and(0<targetY<originalImage.size[1])):
                                dilationImage.putpixel((targetX, targetY), 1)
    return dilationImage