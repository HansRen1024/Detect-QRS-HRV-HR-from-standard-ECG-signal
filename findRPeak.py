#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:35:57 2018

@author: hans
"""
import matplotlib.pyplot as plt
import numpy as np
def findRPeak(TimeList,ECGlist):
    num=2000
    x=np.array(TimeList[0:num])
    y=np.array(ECGlist[0:num])
    RMax=max(ECGlist[0:num])
    RMaxIndex=[]
    RPeakIndexList=[]
    xMax=[]
    yMax=[]
    for i in range(num):
        if ECGlist[i]>RMax*0.5: #0.5 is depended on situation.
            RMaxIndex.append(i)
    tempIndex=[RMaxIndex[0]]
    for i in range(1,len(RMaxIndex)+1):
        if i<len(RMaxIndex):
            if RMaxIndex[i]-RMaxIndex[i-1]<50:
                tempIndex.append(RMaxIndex[i])
                continue
            elif len(tempIndex)==0:
                tempIndex.append(RMaxIndex[i])
        tempECG=[]
        for ind in tempIndex:
            tempECG.append(y[ind])
        tempRPeakIndex=tempECG.index(max(tempECG))
        RPeakIndexList.append(tempIndex[tempRPeakIndex])
        tempIndex=[]
    for j in RPeakIndexList:
        xMax.append(x[j])
        yMax.append(y[j])
    plt.plot(x,y,'b',xMax, yMax, 'or')
    plt.show()
