#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt


# In[99]:


data = pd.read_csv(r"C:\Users\DELL\Desktop\BackOrders.csv")


# In[100]:


data.isnull()


# In[101]:


data.isnull().sum()


# In[102]:


remove=['lead_time']
data.drop(remove,inplace=True,axis=1)


# In[103]:


data.duplicated()


# In[104]:


df = pd.read_csv(r"C:\Users\DELL\Desktop\BackOrders.csv")


# In[105]:



df=df.groupby('lead_time')['in_transit_qty'].sum().to_frame().reset_index()


plt.barh(df['lead_time'],df['in_transit_qty'],color = ['#F0F8FF','#E6E6FA','#B0E0E6']) 

plt.title('Chart title')
plt.xlabel('X axis title')
plt.ylabel('Y axis title') 

plt.show()


# In[107]:



sns.barplot(x = 'lead_time',y = 'in_transit_qty',data =df,palette = "Blues")

plt.title('Chart title')
plt.xlabel('X axis title')
plt.ylabel('Y axis title') 
plt.xticks(rotation=90)

plt.show()


# In[108]:



plt.scatter(df['lead_time'],df['in_transit_qty'],alpha=0.5 )

plt.title('Chart title')
plt.xlabel('X axis title')
plt.ylabel('Y axis title') 

plt.show()


# In[ ]:




