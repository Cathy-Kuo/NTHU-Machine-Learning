#!/usr/bin/env python
# coding: utf-8

# In[90]:


import string
from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt


# In[91]:


f = open('hw3_dataset.txt', "r")
lines = f.readlines()
f.close()
trainingSet=[]
C=[0] * 20
a = 0
weight = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
for line in lines:
    sum = 0
    trainingSet.append([1, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9])])
    for j in range(5, 10):
        sum+= int(line[j])
    if sum >2:
        C[a] = 1
    else:
        C[a] = 0
    a+=1


# In[92]:


def CH(pos, data):
    h = 0
    for i in range(6):
        h+=round((weight[i]*data[i]), 1)
    h = round(h, 1)
    if h<=0:
        h = 0
    else:
        h = 1
    return (C[pos]-h)


# In[93]:


def Weight(rate, ch, x):
    for i in range(6):
        weight[i] = round ((weight[i] + rate*ch*x[i]), 1)


# In[94]:


for i in range(6):
    weight[i] = 0.2
done = 0
count = 0
rund2 = 0
while done!=1 :
    rund2+=1
    for i in range(20):
        ch = CH(i, trainingSet[i])
        if (ch!=0):
            Weight(0.2, ch, trainingSet[i])
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund2)


# In[95]:


for i in range(6):
    weight[i] = 0.2
done = 0
count = 0
rund4 = 0
while done!=1 :
    rund4+=1
    for i in range(20):
        ch = CH(i, trainingSet[i])
        if (ch!=0):
            Weight(0.4, ch, trainingSet[i])
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund4)


# In[96]:


for i in range(6):
    weight[i] = 0.2
done = 0
count = 0
rund6 = 0
while done!=1 :
    rund6+=1
    for i in range(20):
        ch = CH(i, trainingSet[i])
        if (ch!=0):
            Weight(0.6, ch, trainingSet[i])
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund6)


# In[97]:


for i in range(6):
    weight[i] = 0.2
done = 0
count = 0
rund8 = 0
while done!=1 :
    rund8+=1
    for i in range(20):
        ch = CH(i, trainingSet[i])
        if (ch!=0):
            Weight(0.8, ch, trainingSet[i])
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund8)


# In[98]:


for i in range(6):
    weight[i] = 0.2
done = 0
count = 0
rund1 = 0
while done!=1 :
    rund1+=1
    for i in range(20):
        ch = CH(i, trainingSet[i])
        if (ch!=0):
            Weight(1.0, ch, trainingSet[i])
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund1)


# In[99]:


plt.plot([0.2, 0.4, 0.6, 0.8, 1.0], [rund2, rund4, rund6, rund8, rund1])
plt.ylabel('example-presentations')
plt.xlabel('learning-rate')
plt.show()


# In[ ]:




