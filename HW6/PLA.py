#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
from sklearn.datasets import load_digits
import random
import csv


# In[2]:


with open("training-data.txt") as csvfile:
    lines=csv.reader(csvfile)
    dataset = list(lines)
trainingSet = []
C=[0] * 90
rate = 0.2
weight = [0.2]*5
for i in range(len(dataset)):
    if (i>=0 and i<45):
        trainingSet.append([1, float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        C[i] = 0
    else:
        trainingSet.append([1, float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        C[i] = 1


# In[3]:


with open("testing-data.txt") as csvfile:
    lines=csv.reader(csvfile)
    dataset = list(lines)
testSet = []
C_test=[0] * 10
for i in range(len(dataset)):
    if (i>=0 and i<5):
        testSet.append([1, float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        C_test[i] = 0
    else:
        testSet.append([1, float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        C_test[i] = 1


# In[4]:


def CH(pos, data):
    h = 0
    for i in range(5):
        h+=round(weight[i]*data[i], 1)
    h = round(h, 1)
    if h<=2:
        h = 0
    else:
        h = 1
    return (C[pos]-h)


# In[5]:


def Weight(ch, x):
    for i in range(5):
        weight[i] = round ((weight[i] + rate*ch*x[i]), 1)


# In[6]:


done = 0
count = 0
rund = 10000
while (done!=1) :
    for i in range(90):
        ch = CH(i, trainingSet[i])
        if (ch!=0):
            Weight(ch, trainingSet[i])
            count = 0
        else:
            count+=1
        if (count==90 or rund==0):
            done = 1
    rund = rund-1


# In[7]:


h_test = [0]*10
error = 0
for i in range (10):
    sig = 0
    for j in range(5):
        sig += weight[j] * testSet[i][j]
    if (sig>0):
        h_test[i] = 1
    if h_test[i]!= C_test[i]:
        error+=1
print ("Accuracy of PLA:", error/10*100, "%")


# In[ ]:




