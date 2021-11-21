#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_excel('desktop/predict.xlsx', sheet_name=0)


# In[5]:


df


# In[6]:


df.info()


# In[7]:


df.shape


# In[9]:


df.isnull().sum()


# In[10]:


#Separate the null values from dataframe (df) and create a variable “test data”


# In[14]:


test_data = df[df['C'].isnull()]


# In[15]:


test_data


# In[16]:


#Drop the null values from the dataframe (df) and represent as ‘train data”


# In[21]:


df.dropna(inplace=True)


# In[22]:


df


# In[23]:


#Create “x_train” & “y_train” from train data.


# In[24]:


x_train = df.drop('C',axis=1)


# In[25]:


x_train


# In[26]:


y_train = df['C']


# In[27]:


y_train


# In[28]:


#Build the linear regression model


# In[29]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()


# In[30]:


lr.fit(x_train, y_train)


# In[31]:


#Create the x_test from test data


# In[33]:


x_test = test_data[['A','B']]


# In[34]:


x_test


# In[35]:


#Apply the model on x_test of test data to make predictions.


# In[36]:


y_pred = lr.predict(x_test)


# In[37]:


y_pred


# In[ ]:


#Replace the missing values with predicted values.


# In[47]:


test_data['y_pred'] = y_pred


# In[45]:


test_data


# In[46]:


#Gracias


# In[ ]:




