# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:35:57 2018

@author: hans
"""
import matplotlib.pyplot as plt
import numpy as np
def findR(TimeList,ECGlist):
    RMax=max(ECGlist)
    RMaxIndex=[]
    RPeakIndexList=[]
    xMax=[]
    yMax=[]
    for i in range(len(ECGlist)):
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
            tempECG.append(ECGlist[ind])
        tempRPeakIndex=tempECG.index(max(tempECG))
        RPeakIndexList.append(tempIndex[tempRPeakIndex])
        tempIndex=[]
    for j in RPeakIndexList:
        xMax.append(np.array(TimeList)[j])
        yMax.append(np.array(ECGlist)[j])
    return xMax,yMax,RPeakIndexList
def findQS(TimeList,ECGlist,RPeakIndexList):
    fs=250
    l=len(ECGlist)
    QxMin=[]
    QyMin=[]
    SxMin=[]
    SyMin=[]
    for ind in RPeakIndexList:
        w1=fs/10
        w2=fs/5
        if ind<w1:
            w1=ind
        if ind < w2:
            w2=ind
        if ind+w1>l:
            w1=l-ind-1
        if ind+w2>l:
            w2=l-ind-1
        w1TempQ=[]
        w1TempS=[]
        w2TempQ=[]
        w2TempS=[]
        for i in range(int(w1)):
            w1TempQ.append([ECGlist[ind-i],ind-i])
            w1TempS.append([ECGlist[ind+i],ind+i])
        for j in range(int(w2)):
            w2TempQ.append([ECGlist[ind-i],ind-i])
            w2TempS.append([ECGlist[ind+i],ind+i])
        w1Qmin=min(w1TempQ)
        w1Smin=min(w1TempS)
        w2Qmin=min(w2TempQ)
        w2Smin=min(w2TempS)
        wQmin=min([w1Qmin,w2Qmin])
        QxMin.append(TimeList[wQmin[1]])
        QyMin.append(ECGlist[wQmin[1]])
        QIndex.append(wQmin[1])
        wSmin=min([w1Smin,w2Smin])
        SxMin.append(TimeList[wSmin[1]])
        SyMin.append(ECGlist[wSmin[1]])
        SIndex.append(wSmin[1])
    return QxMin,QyMin,SxMin,SyMin
            
def findQRS(TimeList，ECGlist):
    num=1000
    x=np.array(TimeList[0:num])
    y=np.array(ECGlist[0:num])
    RxMax,RyMax,RPeakIndexList=findR(TimeList[0:num],ECGlist[0:num])
    QxMin,QyMin,SxMin,SyMin=findQS(TimeList[0:num],ECGlist[0:num],RPeakIndexList)
    plt.plot(x,y,'b',RxMax, RyMax, 'or',QxMin,QyMin,'xg',SxMin,SyMin,'.k')
    plt.show()
