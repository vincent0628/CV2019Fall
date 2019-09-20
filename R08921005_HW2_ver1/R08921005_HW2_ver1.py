# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 19:33:55 2019

@author: vincent黃國郡
"""
from PIL import Image
import numpy as np
import pandas as pd
import cv2
from statistics import mean
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
for r in original_lena_array:
    for pixel in r:
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
height,width=original_lena_array.shape
visited = np.zeros([height,width])
labeledImageArray = np.zeros([height,width])
labelId=1
numberOfLabelDict={}
numberOfCurrentLabel=0
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
                labeledImageArray[xx,yy]=labelId
                numberOfCurrentLabel+=1
                for uu in [xx-1,xx,xx+1]:
                    for vv in [yy-1,yy,yy+1]:
                        if(0<=uu<height)and(0<=vv<width):
                            if (visited[uu,vv]==0)and (binarize_lena_array[uu,vv]!=0):
                                stack.push((uu,vv))
            if (numberOfCurrentLabel>=thresholdRegionPixels):
                numberOfLabelDict[labelId]=numberOfCurrentLabel
            numberOfCurrentLabel=0
            labelId+=1
#   初始畫框框矩陣
rectangles={}  
for key in numberOfLabelDict:
    currentKeyX,currentKeyY=np.where(labeledImageArray == key)
    point1=(min(currentKeyY),min(currentKeyX))
    point2=(max(currentKeyY),max(currentKeyX))
    rectangles[key]=[point1,point2]
   

connected_lena_array = np.zeros((height,width,3))
connected_lena_array[:,:,0]=binarize_lena_array
connected_lena_array[:,:,1]=binarize_lena_array
connected_lena_array[:,:,2]=binarize_lena_array

for points in rectangles:   
    print(rectangles[points][2])
    cv2.rectangle(connected_lena_array, rectangles[points][0],  rectangles[points][1], (255,0, 0), 2)
#    cv2.line(connected_lena_array, rectangles[points][2], , (255,0, 0, ), 5)
Image.fromarray(connected_lena_array.astype(np.uint8)).save('connected_lena.bmp')
    
    
    