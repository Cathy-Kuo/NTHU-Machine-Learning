#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


with open("iris.data.txt") as csvfile:
    lines=csv.reader(csvfile)


# In[3]:


def loadDataset(filename, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if (x%50)<30 :
                trainingSet.append(dataset[x])
            else :
                testSet.append(dataset[x])


# In[4]:


trainingSet=[]
testSet=[]
loadDataset(r'iris.data.txt', trainingSet, testSet)


# In[5]:


import math
def dis(ex1, ex2):
    distance = 0
    for i in range(4):
        distance+=pow((ex1[i]-ex2[i]), 2)
    return math.sqrt(distance)


# In[6]:


def classfier1(ex):
    dist = 1000000
    after = "Iris-setosa"
    for s in trainingSet :
        newdist = dis(ex, s)
        if (newdist<dist):
            dist = newdist
            after = s[4]
    return after
            


# In[7]:


correct = 0
error = 0
for t in testSet:
    origin = t[4]
    get = classfier1(t)
    if (origin==get):
        correct+=1
    else:
        error+=1
correct_rate = correct/60
print("correct number: %d\n" %correct)
print("incorrect number: %d\n" %error)
print("accuracy: %f\n" %correct_rate)


# In[ ]:




