# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:56:19 2019

@author: vincent黃國郡
"""
#    IO input type: Image
#    except kernel: numpy array, centerKernel: tuple

from PIL import Image


def dilation(originalImage, kernel, centerKernel):
    dilationImage = Image.new('1', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            originalPixel = originalImage.getpixel((r, c))
            # If this pixel is 1 which is white
            if (originalPixel != 0):
                for ii in range(kernel.shape[0]):
                    for jj in range(kernel.shape[1]):
                        if (kernel[ii, jj]):
                            targetX = r + (ii - centerKernel[0])
                            targetY = c + (jj - centerKernel[1])
                            if ((0 < targetX < originalImage.size[0])
                                    and (0 < targetY < originalImage.size[1])):
                                dilationImage.putpixel((targetX, targetY), 1)
    return dilationImage


def erosion(originalImage, kernel, centerKernel):
    erosionImage = Image.new('1', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            matchFlag = 1
            for ii in range(kernel.shape[0]):
                for jj in range(kernel.shape[1]):
                    if (kernel[ii, jj] and matchFlag):
                        targetX = r + (ii - centerKernel[0])
                        targetY = c + (jj - centerKernel[1])
                        if ((0 < targetX < originalImage.size[0])
                                and (0 < targetY < originalImage.size[1])):
                            if (originalImage.getpixel(
                                (targetX, targetY)) == 0):
                                matchFlag = False
                                break
                        else:
                            matchFlag = False
                            break
            if (matchFlag):
                erosionImage.putpixel((r, c), 1)
    return erosionImage


def opening(originalImage, kernel, centerKernel):
    return dilation(erosion(originalImage, kernel, centerKernel), kernel, centerKernel)


def closing(originalImage, kernel, centerKernel):
    return erosion(dilation(originalImage, kernel, centerKernel), kernel, centerKernel)

def complement(originalImage):
    complementImage = Image.new('1', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            if (originalImage.getpixel((r, c)) == 0):
                complementImage.putpixel((r, c), 1)
            else:
                complementImage.putpixel((r, c), 0)
    return  complementImage

def intersection(image1, image2):
    intersectionImage = Image.new('1', image1.size)
    for r in range(image1.size[0]):
        for c in range(image1.size[1]):
            image1Pixel = image1.getpixel((r, c))
            image2Pixel = image2.getpixel((r, c))
            if (image1Pixel and image2Pixel):
                intersectionImage.putpixel((r, c), 1)
            else:
                intersectionImage.putpixel((r, c), 0)
    return intersectionImage

def erosionWithCenter(originalImage, kernel, centerKernel):
    erosionImage = Image.new('1', originalImage.size)
    for r in range(originalImage.size[0]):
        for c in range(originalImage.size[1]):
            matchFlag = True
            for x in range(kernel.shape[0]):
                for y in range(kernel.shape[1]):
                    if (kernel[x, y] == 1):
                        destX = r + (x - centerKernel[0])
                        destY = c + (y - centerKernel[1])
                        if ((0 <= destX < originalImage.size[0]) and \
                            (0 <= destY < originalImage.size[1])):
                            if (originalImage.getpixel((destX, destY)) == 0):
                                matchFlag = False
                                break
                        else:
                            matchFlag = False
                            break
            if (matchFlag):
                erosionImage.putpixel((r, c), 1)
    return erosionImage

def hitmiss(originalImage, kernel_J, centerKernel_J, kernel_K, centerKernel_K):
    return  intersection(erosion(originalImage, kernel_J, centerKernel_J),
                         erosion(complement(originalImage), kernel_K, centerKernel_K))