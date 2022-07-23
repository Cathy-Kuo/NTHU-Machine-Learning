#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import math
import csv
import random
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


with open("training-data.txt") as csvfile:
    lines=csv.reader(csvfile)
    dataset = list(lines)
training = []
class_train = [0]*90
prob = [1/90]*90
for i in range(len(dataset)):
    if (i>=0 and i<45):
        training.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_train[i] = 1
    else:
        training.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_train[i] = -1


# In[3]:


with open("testing-data.txt") as csvfile:
    lines1=csv.reader(csvfile)
    dataset = list(lines1)
test = []
class_test = [0]*10
for i in range(len(dataset)):
    if (i>=0 and i<5):
        test.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_test[i] = 1
    else:
        test.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_test[i] = -1


# In[4]:


#k-NN


# In[5]:


e = [0]*90
testAttr=[[0]*9 for i in range(10)]
a = [0]*9


# In[6]:


def takeSecond(elem):
    return elem[1]


# In[7]:


def dis(ex1, ex2):
    distance = 0
    for i in range(4):
        distance+=pow((ex1[i]-ex2[i]), 2)
    return math.sqrt(distance)


# In[8]:


def kNN(ex, adaSet):
    ansset = []
    ans = [0]*2
    label = 1
    for i in range(10) :
        dist = dis(ex, training[adaSet[i]])
        ansset.append([class_train[adaSet[i]], dist])
    ansset.sort(key=takeSecond)
    for j in range(3):
        if ansset[j][0]==1:
            ans[0]+=1;
        else:
            ans[1]+=1;
    if ans[0]<ans[1]:
        label = -1
    return label


# In[9]:


def normalize(pro):
    sum = 0
    for i in range(90):
        sum+=pro[i]
    for j in range(90):
        pro[j] = (1/sum)*pro[j]
    return pro


# In[10]:


for i in range(9):
    err = 0
    adaSet = np.random.choice(90, 10, replace=True, p=prob)
    for testing in range(10):
        testAttr[testing][i] = kNN(test[testing], adaSet)
    for j in range(90):
        if class_train[j] == kNN(training[j], adaSet):
            e[j] = 0
        else:
            e[j] = 1
        err = err + prob[j]*e[j]
    a[i] = math.log((1-err)/err)
    b = math.sqrt(err/(1-err))/2
    if b!=0:
        for k in range(90):
            if e[k]==0:
                prob[k] = b*prob[k]
        prob = normalize(prob)


# In[11]:


h_test = [1]*10
error = 0
for i in range (10):
    sig = 0
    for j in range(9):
        sig += a[j] * testAttr[i][j]
    if (sig<=0):
        h_test[i] = -1
    if h_test[i]!= class_test[i]:
        error+=1
acc = 10-error
print ("Accuracy of original adaboost:", acc/10*100, "%")


# In[ ]:




