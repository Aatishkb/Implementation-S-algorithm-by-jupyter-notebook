#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np


# In[14]:


data = pd.read_csv(r'C:\Users\kumar\Desktop\DataSet\lab1.csv')   # path + \fileName with Extension 


# In[15]:


data


# In[16]:


# table is converted into array; : means all Rows&clounm from start , :-1 means not tale last cloumn
array = np.array(data)[:,:-1] 


# In[17]:


array  # in this array last cloumn is not present


# In[18]:


target = np.array(data)[:,-1]  
# we have to take target(go outside or not) but s algorithm only consider +ve target
# : print all rowCloumn but due to -1 last clounm is not considered


# In[19]:


target


# In[1]:


def train(a,t):
    for i,val in enumerate(t):
        if val=='Yes':
            h=a[i].copy()
            break
            
    for i,val in enumerate(a):
                if t[i]=='Yes':
                    for j in range(len(h)):
                        if val[j]!=h[j]:
                            h[j]='?'
                        else:
                            pass
    return h
        


# In[21]:


print(train(array,target))


# In[22]:


print("The Final Hypothesis is : ",train(array,target))

