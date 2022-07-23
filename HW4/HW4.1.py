#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
import math
import csv
import random
import matplotlib.pyplot as plt


# In[2]:


with open("iris.data.txt") as csvfile:
    lines=csv.reader(csvfile)
    dataset = list(lines)
x=[]
t = []
psum = 0
nsum = 0
i = 0
for i in range(len(dataset)-1):
    x.append([float(dataset[i][0]), float(dataset[i][1]), float(dataset[i][2]), float(dataset[i][3])])
    if (i>=0 and i<50):
        t.append([1, 0, 0])
    elif (i>=50 and i<100):
        t.append([0, 1, 0])
    else:
        t.append([0, 0, 1])
    i+=1


# In[3]:


def F(nid):
    #3
    for i in range(4):
        sig = 0
        for j in range(4):
            sig+=x[nid][j]*weight3[j][i]
        e = math.exp(-sig)
        h[nid][i] = 1/(1+e)
    #2
    for i in range(4):
        sig = 0
        for j in range(4):
            sig+=h[nid][j]*weight2[j][i]
        e = math.exp(-sig)
        g[nid][i] = 1/(1+e)
    #1
    for i in range(3):
        sig = 0
        for j in range(4):
            sig+=g[nid][j]*weight1[j][i]
        e = math.exp(-sig)
        y[nid][i] = 1/(1+e)


# In[4]:


def S(nid):
    #1
    for i in range(3):
        s1[nid][i] = y[nid][i]*(1-y[nid][i])*(t[nid][i]-y[nid][i])
    #2
    for j in range(4):
        sig = 0
        for i in range(3):
            sig+=s1[nid][i]*weight1[j][i]
        s2[nid][j] =g[nid][j]*(1-g[nid][j])*sig
   #3
    for j in range(4):
        sig = 0
        for i in range(4):
            sig+=s2[nid][i]*weight2[j][i]
        s3[nid][j] =h[nid][j]*(1-h[nid][j])*sig


# In[5]:


def Weight(lr, nid):
    #1:
    for j in range(4):
        for i in range(3):
            weight1[j][i] = weight1[j][i] + lr*s1[nid][i]*g[nid][j]
    #2
    for j in range(4):
        for i in range(4):
            weight2[j][i] = weight2[j][i] + lr*s2[nid][i]*h[nid][j]
    #3
    for j in range(4):
        for i in range(4):
            weight3[j][i] = weight3[j][i] + lr*s3[nid][i]*x[nid][j]


# In[6]:


def Mse():
    sum1 = 0
    for i in range(150):
        F(i)
        m = 0
        for j in range(3):
            m+=pow((y[i][j]-t[i][j]), 2)
        sum1+=(m/3)
    sum1 = sum1/150
    return sum1


# In[7]:


print("learning-rate : 0.1")
h = [] 
g = []
y = []
s1 = []
s2 = []
s3 = []
weight1 = []
weight2 = []
weight3 = []
for i in range(4):
    weight1.append([random.uniform(-0.1,0.1), random.uniform(-0.1,0.1), random.uniform(-0.1,0.1)])
    weight2.append([random.uniform(-0.1,0.1), random.uniform(-0.1,0.1), random.uniform(-0.1,0.1), random.uniform(-0.1,0.1)])
    weight3.append([random.uniform(-0.1,0.1), random.uniform(-0.1,0.1), random.uniform(-0.1,0.1), random.uniform(-0.1,0.1)])
for i in range(150):
    h.append([0, 0, 0, 0])
    g.append([0, 0, 0, 0])
    y.append([0, 0, 0, 0])
    s1.append([0, 0, 0])
    s2.append([0, 0, 0, 0])
    s3.append([0, 0, 0, 0])
converge = 0
epoch = 0
while converge==0:
    epoch+=1
    print("epoch : ", epoch, end=" ")
    nsum = 0
    for i in range(150):
        F(i)
        S(i)
        Weight(0.1, i)
    nsum = Mse()
    if epoch>1:
        tmp = (nsum-psum)/psum
        tmp = abs(tmp)
        print("The absolute fraction of change in MSE : ", tmp)
        if tmp<=0.0001:
            converge=1
    else:
        print("The absolute fraction of change in MSE : ", "X")
    psum = nsum
print("Total epoch : ", epoch)


# In[ ]:




