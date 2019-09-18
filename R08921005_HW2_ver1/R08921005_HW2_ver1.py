# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:33:55 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np
import pandas as pd
import os


lena_pic = Image.open( "lena.bmp" )
original_lena_array = np.array(lena_pic)

#(a)    a binary image (threshold at 128)
binarize_lena= original_lena_array.copy()
for ii in range(len(original_lena_array)):
    for jj in range(len(original_lena_array[ii])):
        if (original_lena_array[ii][jj]>=128):
            binarize_lena[ii][jj]=255
        else:
            binarize_lena[ii][jj]=0
Image.fromarray(binarize_lena.astype(np.uint8)).save('binarize_lena.bmp')

#(b)    a histogram
histogram = np.zeros(256)
for row in original_lena_array:
    for pixel in row:
        histogram[pixel] += 1
        
df = pd.DataFrame(histogram,columns=['value'])
df.to_csv('histogram.csv')
ax = df.plot.bar(y='value', rot=0)
ticks = ax.xaxis.get_ticklocs()
ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
ax.xaxis.set_ticks(ticks[::50])
ax.xaxis.set_ticklabels(ticklabels[::50])
fig = ax.get_figure()
fig.savefig("histogram.png")

