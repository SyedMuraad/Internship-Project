#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
import numpy as np 
import pandas as pd
import seaborn as sns


# In[12]:


get_ipython().system('pip install streamlit')


# In[16]:


st.title('Amazing Mart Dataset')


# In[27]:


data = pd.read_csv(' Order_csv.csv')
data          


# In[37]:


st.subheader('Raw data')
st.write(data)


# In[38]:


data.columns


# In[39]:


st.subheader('Days to Ship')


# In[48]:


st.subheader('Country')


# In[54]:


my_dataframe = data
st.dataframe(my_dataframe)


# In[ ]:




