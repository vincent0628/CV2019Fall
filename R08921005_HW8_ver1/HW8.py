# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:34:17 2019

@author: vincent
"""

import cv2
import numpy as np
import math

kernel = [(-1,-2), (0,-2), (1,-2),
          (-2,-1), (-1,-1), (0,-1), (1,-1), (2,-1),
          (-2,0), (-1,0), (0,0), (1,0), (2,0),
          (-2,1), (-1,1), (0,1), (1,1), (2,1),
          (-1,2), (0,2), (-1,2)]


def gaussian_noise(img, amplitude):
    r, c = img.shape
    gaussianNoiseImg = np.zeros(img.shape, dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            
            value = img[i][j] + amplitude*np.random.normal(0.0, 1.0, None)

            if value > 255:
                gaussianNoiseImg[i][j] = 255
            else:
                gaussianNoiseImg[i][j] = value

    return gaussianNoiseImg

def salt_pepper(img, prob):
    r, c = img.shape
    saltPepperImg  = np.zeros(img.shape, dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            
            value = np.random.uniform(0.0, 1.0, None)

            if value < prob:
                saltPepperImg[i][j] = 0
            elif value > 1-prob:
                saltPepperImg[i][j] = 255
            else:
                saltPepperImg[i][j] = img[i][j]
    return saltPepperImg

def box_filter(img, size):
    r, c = img.shape
    boxFilterImg  = np.zeros(img.shape, dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            box_range = int(size/2)
            total = 0
            count = 0
            for m in range(-box_range, box_range+1):
                for n in range(-box_range, box_range+1):
                    if 0 <= i+m < r and j+n < c:
                        total += img[i+m][j+n]
                        count += 1
            boxFilterImg[i][j] = int(total / count)
    return boxFilterImg

def median_filter(img, size):
    r, c = img.shape
    medianFilterImg  = np.zeros(img.shape, dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            box_range = int(size/2)
            value = []

            for m in range(-box_range, box_range+1):
                for n in range(-box_range, box_range+1):
                    if 0 <= i+m < r and j+n < c:
                        value.append(img[i+m][j+n])
            value.sort()
            length = len(value)
            mid = int(length/2)

            if length % 2 == 0:
                medianFilterImg [i][j] = int((int(value[mid-1]) + int(value[mid])) / 2)
            else:
                medianFilterImg [i][j] = value[mid]
    return medianFilterImg 

def dilation(img):
    r, c = img.shape
    dilation_img = np.zeros(img.shape, dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            if img[i][j] != 0:
                maximum = 0
                for x, y in kernel:
                    if 0 <= i+x < r and 0 <= j+y < c:
                        maximum = max(maximum, img[i+x][j+y])
                for x, y in kernel:
                    if 0 <= i+x < r and 0 <= j+y < c:
                        dilation_img[i+x][j+y] = maximum
    return dilation_img

def erosion(img):
    r, c = img.shape
    erosion_img = np.zeros(img.shape, dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            set_to_min = True
            minimum = 255
            for x, y in kernel:
                if 0 <= i+x < r and 0 <= j+y < c:
                    minimum = min(minimum, img[i+x][j+y])
                    if img[i+x][j+y] == 0:
                        set_to_min = False
                        break
                else:
                    set_to_min = False
                    break
            
            if set_to_min:
                erosion_img[i][j] = minimum
    return erosion_img

def opening(img):
    return dilation(erosion(img))

def closing(img):
    return  erosion(dilation(img))

def SNR(img, noise_img):
    r, c = img.shape
    n = r * c
    u_img = 0
    u_noise_img = 0
    for i in range(r):
        for j in range(c):
            u_img += img[i][j]
            u_noise_img += int(noise_img[i][j]) - int(img[i][j])
    u_img /= n
    u_noise_img /= n
    VS = 0
    VN = 0
    for i in range(r):
        for j in range(c):
            VS += (int(img[i][j]) - u_img) ** 2
            VN += (int(noise_img[i][j]) - int(img[i][j]) - u_noise_img) ** 2
    VS /= n
    VN /= n
    return 20*math.log10(math.sqrt(VS)/math.sqrt(VN))


if __name__=='__main__':

    lena = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)

    gaussian_10 = gaussian_noise(lena, 10)
    gaussian_30 = gaussian_noise(lena, 30)
    salt_pepper_010 = salt_pepper(lena, 0.1)
    salt_pepper_005 = salt_pepper(lena, 0.05)


    box_3_gaussian_10 = box_filter(gaussian_10, 3)
    box_3_gaussian_30 = box_filter(gaussian_30, 3)
    box_3_saltpepper_010 = box_filter(salt_pepper_010, 3)
    box_3_saltpepper_005 = box_filter(salt_pepper_005, 3)
    box_5_gaussian_10 = box_filter(gaussian_10, 5)
    box_5_gaussian_30 = box_filter(gaussian_30, 5)
    box_5_saltpepper_010 = box_filter(salt_pepper_010, 5)
    box_5_saltpepper_005 = box_filter(salt_pepper_005, 5)
    
    median_3_gaussian_10 = median_filter(gaussian_10, 3)
    median_3_gaussian_30 = median_filter(gaussian_30, 3)
    median_3_saltpepper_010 = median_filter(salt_pepper_010, 3)
    median_3_saltpepper_005 = median_filter(salt_pepper_005, 3)
    median_5_gaussian_10 = median_filter(gaussian_10, 5)
    median_5_gaussian_30 = median_filter(gaussian_30, 5)
    median_5_saltpepper_010 = median_filter(salt_pepper_010, 5)
    median_5_saltpepper_005 = median_filter(salt_pepper_005, 5)
    
    closing_opening_gaussian_10 = closing(opening(gaussian_10))
    closing_opening_gaussian_30 = closing(opening(gaussian_30))
    closing_opening_saltpepper_010 = closing(opening(salt_pepper_010))
    closing_opening_saltpepper_005 = closing(opening(salt_pepper_005))
    opening_closing_gaussian_10 = opening(closing(gaussian_10))
    opening_closing_gaussian_30 = opening(closing(gaussian_30))
    opening_closing_saltpepper_010 = opening(closing(salt_pepper_010))
    opening_closing_saltpepper_005 = opening(closing(salt_pepper_005))

    

    image=[gaussian_10, gaussian_30, salt_pepper_010, salt_pepper_005,
          box_3_gaussian_10, box_3_gaussian_10, box_3_saltpepper_010, box_3_saltpepper_005,
          box_5_gaussian_10, box_5_gaussian_30, box_5_saltpepper_010, box_5_saltpepper_005,
          median_3_gaussian_10, median_3_gaussian_30, median_3_saltpepper_010, median_3_saltpepper_005,
          median_5_gaussian_10, median_5_gaussian_30, median_5_saltpepper_010, median_5_saltpepper_005,
          closing_opening_gaussian_10, closing_opening_gaussian_30, closing_opening_saltpepper_010, closing_opening_saltpepper_005,      
          opening_closing_gaussian_10, opening_closing_gaussian_30, opening_closing_saltpepper_010, opening_closing_saltpepper_005]
    
    imageName = ['gaussian_10', 'gaussian_30', 'salt_pepper_010', 'salt_pepper_005',
                 'box_3_gaussian_10', 'box_3_gaussian_10', 'box_3_saltpepper_010', 'box_3_saltpepper_005',
                 'box_5_gaussian_10', 'box_5_gaussian_30', 'box_5_saltpepper_010', 'box_5_saltpepper_005',
                 'median_3_gaussian_10', 'median_3_gaussian_30', 'median_3_saltpepper_010', 'median_3_saltpepper_005',
                 'median_5_gaussian_10', 'median_5_gaussian_30', 'median_5_saltpepper_010', 'median_5_saltpepper_005',
                 'closing_opening_gaussian_10', 'closing_opening_gaussian_30', 'closing_opening_saltpepper_010','closing_opening_saltpepper_005',      
                 'opening_closing_gaussian_10', 'opening_closing_gaussian_30', 'opening_closing_saltpepper_010', 'opening_closing_saltpepper_005']
    
    f = open('SNR.txt', 'w')
    for name,item in zip(imageName,image):
        cv2.imwrite('output/'+name+'.bmp',item)
        f.writelines(name+'.bmp'+str(SNR(lena,item))+'\n')
    f.close()