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
            originalPixel = originalImage.getpixel(
                (x * sampleFactor, y * sampleFactor))
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
            if ((0 <= targetX < originalImage.size[0]) and
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
    YokoiConnectivityNumber = np.full(originalImage.size, ' ')

    for x in range(originalImage.size[0]):
        for y in range(originalImage.size[1]):
            if (originalImage.getpixel((x, y))):
                neighborhood = getNeighborhood(originalImage, (x, y))
                YokoiConnectivityNumber[y, x] = Yokoi_f(
                    Yokoi_h(neighborhood[0], neighborhood[1],
                            neighborhood[6], neighborhood[2]),
                    Yokoi_h(neighborhood[0], neighborhood[2],
                            neighborhood[7], neighborhood[3]),
                    Yokoi_h(neighborhood[0], neighborhood[3],
                            neighborhood[8], neighborhood[4]),
                    Yokoi_h(neighborhood[0], neighborhood[4], neighborhood[5], neighborhood[1]))
            else:
                YokoiConnectivityNumber[y, x] = ' '

    return YokoiConnectivityNumber


def pairRelationship(matrix):
    """
    type IO numpy array    
    """
    # 1: p, 2: q
    r, c = matrix.shape
    paired_matrix = np.zeros(matrix.shape, dtype=int)
    for i in range(r):
        for j in range(c):
            if matrix[i][j] != '1':      # Yokoi number != 1
                paired_matrix[i][j] = 2  # Set to q
            else:  # Yokoi number == 1
                flag = True
                neighbor4 = [(1, 0), (0, -1), (-1, 0), (0, 1)]
                for m, n in neighbor4:
                    if 0 <= i+m < r and 0 <= j+n < c:
                        if matrix[i+m][j+n] == '1':   # Exist a neighbor' Yokoi number = 1
                            paired_matrix[i][j] = 1   # Set to p
                            flag = False
                            break
                if flag:
                    paired_matrix[i][j] = 2

    return paired_matrix


def connectedShrink_h(b, c, d, e):
    """
    type of  b,c,d,e: int  return: int
    """
    if b == c and (b != d or b != e):
        return 1
    else:
        return 0


def connectedShrink_f(a1, a2, a3, a4):
    """
    type of  a1, a2, a3, a4: int  return: int
    """
    return [a1, a2, a3, a4].count(1) == 1


def connectedShrink(originalImage, matrix):
    """
    type img: Image,matrix :numpy array   return: Image ,Int
    """
    ImageArray = np.array(originalImage)
    r, c = ImageArray.shape
    flag = False
    for i in range(r):
        for j in range(c):
            if ImageArray[i][j] == 1:
                x = [0 for i in range(9)]
                x[0] = ImageArray[i][j]
                index = 0
                neighbor8 = [(1, 0), (0, -1), (-1, 0), (0, 1),
                             (1, 1), (1, -1), (-1, -1), (-1, 1)]
                for m, n in neighbor8:
                    index += 1
                    if 0 <= i+m < r and 0 <= j+n < c:
                        x[index] = ImageArray[i+m][j+n]

                a1 = connectedShrink_h(x[0], x[1], x[6], x[2])
                a2 = connectedShrink_h(x[0], x[2], x[7], x[3])
                a3 = connectedShrink_h(x[0], x[3], x[8], x[4])
                a4 = connectedShrink_h(x[0], x[4], x[5], x[1])

                number = connectedShrink_f(a1, a2, a3, a4)
                # Yokoi number = 1 (edge) and pair relationship =2
                if number == 1 and matrix[i][j] == 1:
                    ImageArray[i][j] = 0
                    flag = True
    img = Image.fromarray(ImageArray)
    return img, flag


if __name__ == '__main__':
    from PIL import Image
    import numpy as np

    lena = Image.open("lena.bmp")
    binary_lena = lena.point(lambda x: 0 if x < 128 else 255, '1')
    downsampling_image = downsampling(binary_lena, 8)
    downsampling_image.save('downsampling.bmp')
    thinning_image = downsampling_image.copy()
    check = True
    iteration = 1
    while check:
        iteration += 1
        yokoi_matrix = Yokoi(thinning_image)
        paired_matrix = pairRelationship(yokoi_matrix)
        thinning_image, check = connectedShrink(thinning_image, paired_matrix)
    thinning_image.save('thinning.bmp')
