# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:34:17 2019

@author: vincent
"""

import cv2
import numpy as np
import math

kernel = [(-1,-2), (0,-2), (1,-2),
          (-2,-1), (-1,-1), (0,-1),
          (1,-1),  (2,-1), (-2,0), 
          (-1,0), (0,0), (1,0), (2,0),
          (-2,1), (-1,1), (0,1), (1,1), (2,1),
          (-1,2), (0,2), (-1,2)]

def gaussian_noise(img, amplitude):
    r, c = img.shape
    res = np.zeros(img.shape, dtype=np.uint8)

    for i in range(r):
        for j in range(c):
            
            value = img[i][j] + amplitude*np.random.normal(0.0, 1.0, None)

            if value > 255:
                res[i][j] = 255
            else:
                res[i][j] = value

    return res

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

    image = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)

    gaussian_10 = gaussian_noise(image, 10)
    gaussian_30 = gaussian_noise(image, 30)
    
    cv2.imwrite('output/gaussian_10.bmp', gaussian_10)
    cv2.imwrite('output/gaussian_30.bmp', gaussian_30)
    
    f = open('test.txt', 'w')
    f.writelines('gaussian_10.bmp:'+str( SNR(image, gaussian_10))+'\n')
    f.writelines('gaussian_30.bmp:'+str( SNR(image, gaussian_30))+'\n')
    f.close()