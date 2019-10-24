# CV2019Fall

Computer Vision I at NTU 2019 Fall.

## Indrocution

This course has 10 homeworks. The 10 homeworks are as follows:

1. Basic Image Manipulation
2. Basic Image Manipulation

## Table of Contents

<!--ts-->

   1. [Environment](https://github.com/vincent0628/CV2019Fall/blob/master/README.md#environment)
   2. [Basic Image Manipulation](https://github.com/vincent0628/CV2019Fall/blob/master/README.md#hw1-basic-image-manipulation)
   3. [Basic Image Manipulation](https://github.com/vincent0628/CV2019Fall/blob/master/README.md#hw2-basic-image-manipulation)

<!--te-->
## Environment

* Programming Language: Python 3
* Programming IDE: Spyder
* Operating System: Windows 10 x64

## HW1: Basic Image Manipulation

* Part 1 of this homework is writing a program to generate the following images from lena.bmp.
  * Up-side-down lena.bmp.
  * Right-side-left lena.bmp.
  * Diagonally mirrored lena.bmp.
* Part 2 of this homework is using any kind of software to do the following things:
  * Rotate lena.bmp 45 degrees clockwise.
  * Shrink lena.bmp in half.
  * Binarize lena.bmp at 128 to get a binary image.

* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW1_ver1/R08921005_HW1_ver1.py)
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW1_ver1/R08921005_HW1_ver1.pdf)

## HW2: Basic Image Manipulation

* Part 1 of this homework is to binarize lena.bmp with threshold 128 (0-127, 128-255).
* Part 2 of this homework is to draw the histogram of lena.bmp.

* Part 3 of this homework is to find connected components with following rules:
  * Draw bounding box of regions.
  * Draw cross at centroid of regions.
  * Omit regions that have a pixel count less than 500.

* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW2_ver2/R08921005_HW2_ver2.py)
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW2_ver2/R08921005_HW2_ver2.pdf)

## HW3: Histogram Equalization

* This homework is to do histogram equalization with following rules:
  * Do histogram on original lena image.
  * Adjust the brightness of lena.bmp to one-third.
  * Do histogram equalization on dark image.
  * Show the histogram of the final image.
* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW3_ver1/R08921005_HW3_ver1.py)
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW3_ver1/R08921005_HW3_ver1.pdf)

# HW4: Mathematical Morphology - Binary Morphology
* This homework is to do binary morphology with following rules:
   * Please use the octagonal 3-5-5-5-3 kernel.
   * Please use the “L” shaped kernel to detect the upper-right corner for hit-and-miss transform.
   * Please process the white pixels (operating on white pixels).
   * Five images should be included in your report: Dilation, Erosion, Opening, Closing, and Hit-and-Miss.
   
* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW4_ver1/HW4.py)
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW4_ver1/R08921005_HW4_ver1.pdf)


# HW5: Mathematical Morphology - Gray Scaled Morphology

* This homework is to do gray scaled morphology with following rules:
   * Please use the octagonal 3-5-5-5-3 kernel.
   * Please take the local maxima or local minima respectively.
   * Four images should be included in your report: Dilation, Erosion, Opening, and Closing.
  
* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW5_ver1/HW5.py) 
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW5_ver1/R08921005_HW5_ver1.pdf)


# HW6: Yokoi Connectivity Number
* This homework is to do Yokoi connectivity number with following rules:
   * Please binarize leba.bmp with threshold 128.
   * Please down sampling binary.bmp from 512x512 to 64x64, using 8x8 blocks as unit and take the topmost-left pixel as the down sampling data.
   * Print Yokoi connectivity number to text file.
* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW6_ver1/HW6.py)
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW6_ver1/R08921005_HW6_ver1.pdf)


# HW7: Thinning
* This homework is to do thinning operation with following rules:
   * Please binarize leba.bmp with threshold 128.
   * Do thinning operation on binary image.
* [Code](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW7_ver1/HW7.py)
* [Report](https://github.com/vincent0628/CV2019Fall/blob/master/R08921005_HW7_ver1/R08921005_HW7_ver1.pdf)
