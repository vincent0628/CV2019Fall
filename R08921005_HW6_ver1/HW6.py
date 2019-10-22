# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:32:58 2019

@author: vincent黃國郡
"""
def downsampling(originalImage, sampleFactor):
    """
    :originalImage: Image,sampleFactor: int, return Image 
    """
    from PIL import Image
    downsamplingWidth = int(originalImage.size[0] / sampleFactor)
    downsamplingHeight = int(originalImage.size[1] / sampleFactor)
    downsamplingImage = Image.new('1', (downsamplingWidth, downsamplingHeight))
    for x in range(downsamplingWidth):
        for y in range(downsamplingHeight):
            originalPixel = originalImage.getpixel((x * sampleFactor, y * sampleFactor))
            downsamplingImage.putpixel((x, y), originalPixel)
    return downsamplingImage

if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    lena = Image.open("lena.bmp")
    binary_lena = lena.point(lambda x: 0 if x < 128 else 255, '1')
    downsamplingImage = downsampling(binary_lena, 8)
    downsamplingImage.save('downsampling.bmp')

