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

# (a)    a binary image (threshold at 128)
binarize_lena_array = original_lena_array.copy()
for ii in range(len(original_lena_array)):
    for jj in range(len(original_lena_array[ii])):
        if (original_lena_array[ii][jj] >= 128):
            binarize_lena_array[ii][jj] = 255
        else:
            binarize_lena_array[ii][jj] = 0
Image.fromarray(binarize_lena_array.astype(np.uint8)).save('binarize_lena.bmp')

# (b)    a histogram
histogram = np.zeros(256)
for row in original_lena_array:
    for pixel in row:
        histogram[pixel] += 1

df = pd.DataFrame(histogram, columns=['value'])
df.to_csv('histogram.csv')
ax = df.plot.bar(y='value', rot=0)
ticks = ax.xaxis.get_ticklocs()
ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
ax.xaxis.set_ticks(ticks[::50])
ax.xaxis.set_ticklabels(ticklabels[::50])
fig = ax.get_figure()
fig.savefig("histogram.png")

# (c)    connected components


class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


thresholdRegionPixels = 500
visited = np.zeros(original_lena_array.shape)
labeledImageArray = np.zeros(original_lena_array.shape)

for ii in range(len(original_lena_array)):
    for jj in range(len(original_lena_array[ii])):
        if binarize_lena_array[ii, jj] == 0:
            visited[ii, jj] = 1
        elif visited[ii, jj] == 0:
            stack = Stack()
            stack.push((ii, jj))
            while not stack.isEmpty():
                xx, yy = stack.pop()
                if visited[xx, yy] == 1:
                    continue
                visited[xx, yy] = 1
