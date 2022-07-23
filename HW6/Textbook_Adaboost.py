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
        class_train[i] = 0
    else:
        training.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_train[i] = 1


# In[3]:


with open("testing-data.txt") as csvfile:
    lines1=csv.reader(csvfile)
    dataset = list(lines1)
test = []
class_test = [0]*10
for i in range(len(dataset)):
    if (i>=0 and i<5):
        test.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_test[i] = 0
    else:
        test.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
        class_test[i] = 1


# In[4]:


#k-NN


# In[5]:


e = [0]*90
exAttr = [[0]*9 for i in range(90)]
testAttr=[[0]*9 for i in range(10)]


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
    label = 0
    for i in range(10) :
        dist = dis(ex, training[adaSet[i]])
        ansset.append([class_train[adaSet[i]], dist])
    ansset.sort(key=takeSecond)
    #print(ansset)
    for j in range(3):
        if ansset[j][0]==0:
            ans[0]+=1;
        else:
            ans[1]+=1;
    if ans[0]<ans[1]:
        label = 1
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
    #print(adaSet)
    for testing in range(10):
        testAttr[testing][i] = kNN(test[testing], adaSet)
    for j in range(90):
        exAttr[j][i] = kNN(training[j], adaSet)
        #print(i, j, exAttr[0][0])
        if class_train[j] == kNN(training[j], adaSet):
            e[j] = 0
        else:
            e[j] = 1
        err = err + prob[j]*e[j]
    b = err/(1-err)
    if b!=0:
        for k in range(90):
            if e[k]==0:
                prob[k] = b*prob[k]
        prob = normalize(prob)


# In[11]:


w = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
rate = 0.2


# In[12]:


def CH(pos, data):
    h = 0
    for i in range(10):
        if i==0:
            h+=round(w[i], 1)
        else:
            h+=round((w[i]*data[i-1]), 1)
    h = round(h, 1)
    if h<=0:
        h = 0
    else:
        h = 1
    return (class_train[pos]-h)


# In[13]:


def Weight(ch, x):
    for i in range(10):
        if i==0:
            w[i] = round ((w[i] + rate*ch), 1)
        else:
            w[i] = round ((w[i] + rate*ch*x[i-1]), 1)


# In[14]:


done = 0
count = 0
rund = 10000
while (done!=1):
    for i in range(90):
        ch = CH(i, exAttr[i])
        if (ch!=0):
            Weight(ch, exAttr[i])
            count = 0
        else:
            count+=1
        if (count==90 or rund==0):
            done = 1
    rund = rund-1


# In[15]:


h_test = [0]*10
error = 0
for i in range (10):
    sig = 0
    for j in range(9):
        sig += w[j+1] * testAttr[i][j]
    sig += w[0]
    if (sig>0):
        h_test[i] = 1
    if h_test[i]!= class_test[i]:
        error+=1
acc = 10-error
print ("Accuracy of textbook adaboost:", acc/10*100, "%")


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Textbook_Adaboost.ipynb')

