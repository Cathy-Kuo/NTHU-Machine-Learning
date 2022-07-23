#!/usr/bin/env python
# coding: utf-8

# In[41]:


import string
from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import random


# In[42]:


f = open('hw3_dataset.txt', "r")
lines = f.readlines()
f.close()
trainingSet=[]
C=[0] * 20
a = 0
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


# In[43]:


def CH(pos, data, N):
    h = 0
    for i in range(6+N):
        h+=round(weight[i]*data[i], 1)
    h = round(h, 1)
    if h<=0:
        h = 0
    else:
        h = 1
    return (C[pos]-h)


# In[44]:


def Weight(rate, ch, x, N):
    for i in range(6+N):
        weight[i] = round ((weight[i] + rate*ch*x[i]), 1)


# In[45]:


N=1
tSet=[]
for line in lines:
    tSet.append([1, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), random.randint(0,1)])
weight = [0.2] * 7
done = 0
count = 0
rund1 = 0
while done!=1 :
    rund1+=1
    for i in range(20):
        ch = CH(i, tSet[i], N)
        if (ch!=0):
            Weight(0.2, ch, tSet[i], N)
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund1)


# In[46]:


N=5
tSet=[]
for line in lines:
    tSet.append([1, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])
weight = [0.2] * 11
done = 0
count = 0
rund5 = 0
while done!=1 :
    rund5+=1
    for i in range(20):
        ch = CH(i, tSet[i], N)
        if (ch!=0):
            Weight(0.2, ch, tSet[i], N)
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund5)


# In[47]:


N=10
tSet=[]
for line in lines:
    tSet.append([1, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])
weight = [0.2] * 16
done = 0
count = 0
rund10 = 0
while done!=1 :
    rund10+=1
    for i in range(20):
        ch = CH(i, tSet[i], N)
        if (ch!=0):
            Weight(0.2, ch, tSet[i], N)
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund10)


# In[48]:


N=15
tSet=[]
for line in lines:
    tSet.append([1, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])
weight = [0.2] * 21
done = 0
count = 0
rund15 = 0
while done!=1 :
    rund15+=1
    for i in range(20):
        ch = CH(i, tSet[i], N)
        if (ch!=0):
            Weight(0.2, ch, tSet[i], N)
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund15)


# In[49]:


N=20
tSet=[]
for line in lines:
    tSet.append([1, int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)])
weight = [0.2] * 26
done = 0
count = 0
rund20 = 0
while done!=1 :
    rund20+=1
    for i in range(20):
        ch = CH(i, tSet[i], N)
        if (ch!=0):
            Weight(0.2, ch, tSet[i], N)
            count = 0
        else:
            count+=1
        if (count==20):
            done = 1
print(rund20)


# In[50]:


plt.plot([1, 5, 10, 15, 20], [rund1, rund5, rund10, rund15, rund20])
plt.ylabel('example-presentations')
plt.xlabel('N')
plt.show()


# In[ ]:




