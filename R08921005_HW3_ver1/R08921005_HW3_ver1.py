# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:33:55 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np
import pandas as pd

lena_pic = Image.open("lena.bmp")
original_lena_array = np.array(lena_pic)
height,width=original_lena_array.shape

def getHistogram(picArray,name):
    histogram=np.zeros(256)
    for r in picArray:
        for pixel in r:
            histogram[pixel] += 1
    df = pd.DataFrame(histogram, columns=['value'])
    df.to_csv(name+'.csv')
    ax1 = df.plot.bar(y='value', rot=0, width=0.8)
    ticks = ax1.xaxis.get_ticklocs()
    ticklabels = [l.get_text() for l in ax1.xaxis.get_ticklabels()]
    ax1.xaxis.set_ticks(ticks[::50])
    ax1.xaxis.set_ticklabels(ticklabels[::50])
    fig = ax1.get_figure()
    fig.savefig(name+'_histogram.png')
    return(histogram)
    
#(a)    original image and its histogram
name='original_lena'   
getHistogram(original_lena_array,name)

#(b)    image with intensity divided by 3 and its histogram
name='dark_lena'   
dark_lena_array = original_lena_array.copy()
for row in range(height):
    for col in range(width):
        dark_lena_array[row,col]=original_lena_array[row,col]//3
Image.fromarray(dark_lena_array.astype(np.uint8)).save(name+'.bmp')
dark_lena_histogram=getHistogram(dark_lena_array,name)

#(c)    image after applying histogram equalization to (b) and its histogram
name='histeq_lena'  
histeq_lena_array = dark_lena_array.copy()
transformTable = np.zeros(256)
for ii in range(len(transformTable)):
    transformTable[ii] = int(255 * np.sum(dark_lena_histogram[0:ii + 1]) / (width * height))
    
for row in range(height):
    for col in range(width):
        histeq_lena_array[row,col]=transformTable[dark_lena_array[row,col]]
Image.fromarray(histeq_lena_array.astype(np.uint8)).save(name+'.bmp')
histeq_lena_histogram=getHistogram(histeq_lena_array,name)
