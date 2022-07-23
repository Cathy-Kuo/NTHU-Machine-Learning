#!/usr/bin/env python
# coding: utf-8

# In[144]:


import csv
import string
import math


# In[145]:


with open("iris.data.txt") as csvfile:
    lines=csv.reader(csvfile)


# In[146]:


def loadDataset(filename, trainingDtataSet=[], trainingLabelSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            trainingDtataSet.append([dataset[x][0], dataset[x][1], dataset[x][2], dataset[x][3]])
        for i in range(150):
            if i<50:
                trainingLabelSet[i]=0
            elif i>=50 and i <100:
                trainingLabelSet[i]=1
            else:
                trainingLabelSet[i]=2


# In[147]:


def takeSecond(elem):
    return elem[1]


# In[148]:


trainingDtataSet=[]
trainingLabelSet=[0]*150
test=[]
dist = [0]*150
ansset = []
ans = [0]*3
loadDataset(r'iris.data.txt', trainingDtataSet, trainingLabelSet)


# In[149]:


def dis(ex1, ex2):
    distance = 0
    for i in range(4):
        distance+=pow((ex1[i]-ex2[i]), 2)
    return math.sqrt(distance)


# In[150]:


def classfier1(k, ex):
    after = "Iris-setosa"
    for i in range(150) :
        dist[i] = dis(ex, trainingDtataSet[i])
        ansset.append([trainingLabelSet[i], dist[i]])
    ansset.sort(key=takeSecond)
    for i in range(k):
        if ansset[i][0]==0:
            ans[0]+=1;
        elif ansset[i][0]==1:
            ans[1]+=1;
        else:
            ans[2]+=1;
    return ans


# In[151]:


k=input('k:')
k = int(k)
data1 = input('test data1:')
data2 = input('test data2:')
data3 = input('test data3:')
data4 = input('test data4:')
test = [float(data1), float(data2), float(data3), float(data4)]
a = classfier1(k, test)
anskey = 0
f=0
for i in range(3):
    if a[i]>anskey:
        anskey = a[i]
        f = i
if f==0:
    print("Label : Iris-setosa")
elif f==1:
    print("Label : Iris-versicolor")
else:
    print("Label : Iris-virginica")


# In[ ]:




