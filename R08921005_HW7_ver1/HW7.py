# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:32:58 2019

@author: vincent黃國郡
"""
def downsampling(originalImage, sampleFactor):
    """
    originalImage: Image,sampleFactor: int, return Image 
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

def getNeighborhood(originalImage, position):
    """
    originalImage: Image,position: tuple, return  numpy array 
    """
    neighborhood = np.zeros(9)
    x, y = position
    neighborhood = []
    for xx in range(3):
        for yy in range(3):
            targetX = x + (xx - 1)
            targetY = y + (yy - 1)
            if ((0 <= targetX < originalImage.size[0]) and \
                (0 <= targetY < originalImage.size[1])):
                pixelValue = originalImage.getpixel((targetX, targetY))
                neighborhood.append(pixelValue)
            else:
                neighborhood.append(0)
    neighborhood = [
        neighborhood[4], neighborhood[7], neighborhood[3], 
        neighborhood[1], neighborhood[5], neighborhood[8], 
        neighborhood[6], neighborhood[0], neighborhood[2]]
    return neighborhood

def Yokoi_h(b, c, d, e):
    """
    type of  b,c,d,e: int  return: str
    """
    if ((b == c) and (b != d or b != e)):
        return 'q'
    if ((b == c) and (b == d and b == e)):
        return 'r'
    if (b != c):
        return 's'
    
    
def Yokoi_f(a1, a2, a3, a4):
    """
    type of  b,c,d,e: int  return: str
    0: Isolated 1: Edge 2: Connecting 3: Branching 4: Crossing 5:interior
    """
    if (a1 == a2 == a3 == a4 == 'r'):
        return 5
    else:
        return [a1, a2, a3, a4].count('q')
    
def Yokoi(originalImage):
    """
    type originalImage: Image ,return: numpy array
    """    
    YokoiConnectivityNumber = np.full(downsamplingImage.size, ' ')

    for x in range(originalImage.size[0]):
        for y in range(originalImage.size[1]):
            if (originalImage.getpixel((x, y))):
                neighborhood = getNeighborhood(originalImage, (x, y))
                YokoiConnectivityNumber[y, x] = Yokoi_f(
                    Yokoi_h(neighborhood[0], neighborhood[1], neighborhood[6], neighborhood[2]), 
                    Yokoi_h(neighborhood[0], neighborhood[2], neighborhood[7], neighborhood[3]), 
                    Yokoi_h(neighborhood[0], neighborhood[3], neighborhood[8], neighborhood[4]), 
                    Yokoi_h(neighborhood[0], neighborhood[4], neighborhood[5], neighborhood[1]))
            else:
                YokoiConnectivityNumber[y, x] = ' '
    
    return YokoiConnectivityNumber

if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    lena = Image.open("lena.bmp")
    binary_lena = lena.point(lambda x: 0 if x < 128 else 255, '1')
    downsamplingImage = downsampling(binary_lena, 8)
    downsamplingImage.save('downsampling.bmp')
    YokoiConnectivityNumber = Yokoi(downsamplingImage)
    np.savetxt('YokoiConnectivityNumber.txt',YokoiConnectivityNumber,delimiter='',fmt='%s')
