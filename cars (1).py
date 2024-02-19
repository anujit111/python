#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd


# In[22]:


data = pd.read_csv("E:\dataset\cars.csv")


# In[23]:


data


# In[24]:


data.head()


# In[25]:


data.shape


# In[26]:


data.isnull().sum()


# In[56]:


data["Cylinders"].fillna(data["Cylinders"].mean() , inplace = True)


# In[30]:


make_counts = data['Make'].value_counts()


# In[31]:


make_counts 


# In[35]:


filtered_df = data[(data['Origin'] == 'Asia') | (data['Origin'] == 'Europe')]


# In[36]:


filtered_df


# In[42]:


cars_df = data[data['Weight'] <= 4000]


# In[43]:


cars_df


# In[50]:


data['MPG_City'] += 3


# In[51]:


data


# In[55]:





# In[ ]:




