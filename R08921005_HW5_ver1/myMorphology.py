# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:32:58 2019

@author: vincent黃國郡
"""
#    IO input type: Image
#    except kernel: numpy array, centerKernel: tuple

from PIL import Image


def dilation(originalImage, kernel, centerKernel):
    dilationImage = Image.new('L', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            localMaxPixel = 0
            for ii in range(kernel.shape[0]):
                for jj in range(kernel.shape[1]):
                    if (kernel[ii, jj]):
                        targetX = r + (ii - centerKernel[0])
                        targetY = c + (jj - centerKernel[1])
                        if ((0 <= targetX < originalImage.size[0])
                                and (0 <= targetY < originalImage.size[1])):
                            originalPixel = originalImage.getpixel(
                                (targetX, targetY))
                            localMaxPixel = max(originalPixel, localMaxPixel)
            dilationImage.putpixel((r, c), localMaxPixel)
    return dilationImage


def erosion(originalImage, kernel, centerKernel):
    erosionImage = Image.new('L', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            localMinPixel = 255
            for ii in range(kernel.shape[0]):
                for jj in range(kernel.shape[1]):
                    if (kernel[ii, jj]):
                        targetX = r + (ii - centerKernel[0])
                        targetY = c + (jj - centerKernel[1])
                        if ((0 <= targetX < originalImage.size[0])
                                and (0 <= targetY < originalImage.size[1])):
                            originalPixel = originalImage.getpixel(
                                (targetX, targetY))
                            localMinPixel = min(originalPixel, localMinPixel)
            erosionImage.putpixel((r, c), localMinPixel)
    return erosionImage


def opening(originalImage, kernel, centerKernel):
    return dilation(erosion(originalImage, kernel, centerKernel), kernel, centerKernel)


def closing(originalImage, kernel, centerKernel):
    return erosion(dilation(originalImage, kernel, centerKernel), kernel, centerKernel)
