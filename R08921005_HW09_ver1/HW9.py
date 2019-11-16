# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:11:07 2019

@author: vincent
"""
import cv2
import numpy as np
import math
import itertools


def createNeighbor(start, end):
    x = list(range(start, end))
    return list(itertools.product(x, repeat=2))


def robert_operator(img, threshold):
    r, c = img.shape
    robert_img = np.zeros(img.shape, dtype=np.uint8)
    r1_mask = [-1, 0, 0, 1]
    r2_mask = [0, -1, 1, 0]
    for i in range(r):
        for j in range(c):
            candidate = []
            for m, n in neighbor_2:
                if 0 <= i+m < r and 0 <= j+n < c:
                    candidate.append(img[i+m][j+n])
                else:
                    candidate.append(0)
            r1 = 0
            r2 = 0
            for k in range(len(candidate)):
                r1 += int(candidate[k]) * r1_mask[k]
                r2 += int(candidate[k]) * r2_mask[k]
            value = math.sqrt((r1**2) + (r2**2))
            if (value < threshold):
                robert_img[i][j] = 255
    return robert_img


def prewitt_operator(img, threshold):
    r, c = img.shape
    prewitt_img = np.zeros(img.shape, dtype=np.uint8)
    p1_mask = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    p2_mask = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for i in range(r):
        for j in range(c):
            candidate = []
            for m, n in neighbor_3:
                if 0 <= i+m < r and 0 <= j+n < c:
                    candidate.append(img[i+m][j+n])
                else:
                    candidate.append(0)
            p1 = 0
            p2 = 0
            for k in range(len(candidate)):
                p1 += int(candidate[k]) * p1_mask[k]
                p2 += int(candidate[k]) * p2_mask[k]
            value = math.sqrt((p1**2) + (p2**2))
            if (value < threshold):
                prewitt_img[i][j] = 255
    return prewitt_img


def sobel_operator(img, threshold):
    r, c = img.shape
    sobel_img = np.zeros(img.shape, dtype=np.uint8)
    s1_mask = [-1, -2, -1,  0, 0, 0,  1, 2, 1]
    s2_mask = [-1,  0,  1, -2, 0, 2, -1, 0, 1]
    for i in range(r):
        for j in range(c):
            candidate = []
            for m, n in neighbor_3:
                if 0 <= i+m < r and 0 <= j+n < c:
                    candidate.append(img[i+m][j+n])
                else:
                    candidate.append(0)
            s1 = 0
            s2 = 0
            for k in range(len(candidate)):
                s1 += int(candidate[k]) * s1_mask[k]
                s2 += int(candidate[k]) * s2_mask[k]
            value = math.sqrt((s1**2) + (s2**2))
            if (value < threshold):
                sobel_img[i][j] = 255
    return sobel_img


def frei_chen_operator(img, threshold):
    r, c = img.shape
    frei_chen_img = np.zeros(img.shape, dtype=np.uint8)
    number = math.sqrt(2)
    f1_mask = [-1, -number, -1,
               0,       0,  0,
               1,  number,  1]
    f2_mask = [-1, 0,      1,
               -number, 0, number,
               -1, 0,      1]

    for i in range(r):
        for j in range(c):
            candidate = []
            for m, n in neighbor_3:
                if 0 <= i+m < r and 0 <= j+n < c:
                    candidate.append(img[i+m][j+n])
                else:
                    candidate.append(0)
            f1 = 0
            f2 = 0
            for k in range(len(candidate)):
                f1 += int(candidate[k]) * f1_mask[k]
                f2 += int(candidate[k]) * f2_mask[k]
            value = math.sqrt((f1**2) + (f2**2))
            if (value < threshold):
                frei_chen_img[i][j] = 255
    return frei_chen_img


def kirsch_operator(img, threshold):
    r, c = img.shape
    kirsch_img = np.zeros(img.shape, dtype=np.uint8)
    masks = [(-3, -3, 5, -3, 0, 5, -3, -3, 5),
             (-3, 5, 5, -3, 0, 5, -3, -3, -3),
             (5, 5, 5, -3, 0, -3, -3, -3, -3),
             (5, 5, -3, 5, 0, -3, -3, -3, -3),
             (5, -3, -3, 5, 0, -3, 5, -3, -3),
             (-3, -3, -3, 5, 0, -3, 5, 5, -3),
             (-3, -3, -3, -3, 0, -3, 5, 5, 5),
             (-3, -3, -3, -3, 0, 5, -3, 5, 5)]
    for i in range(r):
        for j in range(c):
            value = 0
            for mask in masks:
                candidate = []
                for m, n in neighbor_3:
                    if 0 <= i+m < r and 0 <= j+n < c:
                        candidate.append(img[i+m][j+n])
                    else:
                        candidate.append(0)
                g = 0
                for k in range(len(candidate)):
                    g += int(candidate[k]) * mask[k]
                value = max(value, g)
            if (value < threshold):
                kirsch_img[i][j] = 255

    return kirsch_img


def robinson_operator(img, threshold):
    r, c = img.shape
    robinson_img = np.zeros(img.shape, dtype=np.uint8)
    masks = [(-1, 0, 1, -2, 0, 2, -1, 0, 1),
             (0, 1, 2, -1, 0, 1, -2, -1, 0),
             (1, 2, 1, 0, 0, 0, -1, -2, -1),
             (2, 1, 0, 1, 0, -1, 0, -1, -2),
             (1, 0, -1, 2, 0, -2, 1, 0, -1),
             (0, -1, -2, 1, 0, -1, 2, 1, 0),
             (-1, -2, -1, 0, 0, 0, 1, 2, 1),
             (-2, -1, 0, -1, 0, 1, 0, 1, 2)]
    for i in range(r):
        for j in range(c):
            value = 0
            for mask in masks:
                candidate = []
                for m, n in neighbor_3:
                    if 0 <= i+m < r and 0 <= j+n < c:
                        candidate.append(img[i+m][j+n])
                    else:
                        candidate.append(0)
                g = 0
                for k in range(len(candidate)):
                    g += int(candidate[k]) * mask[k]
                value = max(value, g)
            if (value < threshold):
                robinson_img[i][j] = 255

    return robinson_img


def nevatia_babu_operator(img, threshold):
    r, c = img.shape
    nevatia_babu_img = np.zeros(img.shape, dtype=np.uint8)
    masks = [(100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, -100, -100, -100, -100, -100, -100, -100, -100, -100, -100),
             (100, 100, 100, 100, 100, 100, 100, 100, 78, -32, 100, 92, 0, -
              92, -100, 32, -78, -100, -100, -100, -100, -100, -100, -100, -100),
             (100, 100, 100, 32, -100, 100, 100, 92, -78, -100, 100, 100, 0, -
              100, -100, 100, 78, -92, -100, -100, 100, -32, -100, -100, -100),
             (-100, -100, 0, 100, 100, -100, -100, 0, 100, 100, -100, -100,
              0, 100, 100, -100, -100, 0, 100, 100, -100, -100, 0, 100, 100),
             (-100, 32, 100, 100, 100, -100, -78, 92, 100, 100, -100, -100, 0,
              100, 100, -100, -100, -92, 78, 100, -100, -100, -100, -32, 100),
             (100, 100, 100, 100, 100, -32, 78, 100, 100, 100, -100, -92, 0, 92, 100, -100, -100, -100, -78, 32, -100, -100, -100, -100, -100)]
    for i in range(r):
        for j in range(c):
            value = 0
            for mask in masks:
                candidate = []
                for m, n in neighbor_5:
                    if 0 <= i+m < r and 0 <= j+n < c:
                        candidate.append(img[i+m][j+n])
                    else:
                        candidate.append(0)
                g = 0
                for k in range(len(candidate)):
                    g += int(candidate[k]) * mask[k]
                value = max(value, g)
            if (value < threshold):
                nevatia_babu_img[i][j] = 255

    return nevatia_babu_img


if __name__ == '__main__':
    neighbor_2 = createNeighbor(0, 2)
    neighbor_3 = createNeighbor(-1, 2)
    neighbor_5 = createNeighbor(-2, 3)

    lena = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)

    robert = robert_operator(lena, 25)
    cv2.imwrite('Robert.bmp', robert)

    prewitt = prewitt_operator(lena, 100)
    cv2.imwrite('Prewitt.bmp', prewitt)

    sobel = sobel_operator(lena, 100)
    cv2.imwrite('Sobel.bmp', sobel)

    frei_chen = frei_chen_operator(lena, 100)
    cv2.imwrite('Frei and Chen.bmp', frei_chen)

    kirsch = kirsch_operator(lena, 300)
    cv2.imwrite('Kirsch.bmp', kirsch)

    robinson = robinson_operator(lena, 100)
    cv2.imwrite('Robinson.bmp', robinson)

    nevatia_babu = nevatia_babu_operator(lena, 15000)
    cv2.imwrite('Nevatia-Babu.bmp', nevatia_babu)
