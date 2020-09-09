#!/usr/bin/env python
# coding: utf-8

# # Linear Regression of SAT Score/GPA
# 

# In[83]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
sns.set()


# In[84]:


data= pd.read_csv ("C:/Users/Brendon/Desktop/1.01. Simple linear regression.csv")


# In[85]:


data


# In[86]:


data.describe()


# In[87]:


y=data['GPA']
x1=data['SAT']
plt.scatter(x1,y)
plt.xlabel('SAT SCORE')
plt.ylabel('GPA')
plt.plot()


# In[88]:


x=sm.add_constant(x1)
results=sm.OLS(y,x).fit()
results.summary()


# In[89]:


plt.scatter(x1,y)
y=0.0017*x1+0.275
fig=plt.plot(x1,y, lw=3,c='red',label='regression line')
plt.xlabel('SAT',fontsize=15)
plt.ylabel('GPA',fontsize=15)
plt.title('Regression Model of SAT score vs. GPA')
plt.show()


# In[102]:


print(0.0017*(1650)+0.275 ) 


# # Linear Regression Real Estate Prices
# 

# In[90]:


data_2= pd.read_csv ("C:/Users/Brendon/Desktop/real_estate_price_size.csv")


# In[91]:


data_2


# In[92]:


data_2.describe()


# In[93]:


y1=data_2['price']
x2=data_2['size']
plt.scatter(x2,y1)
plt.xlabel('size(Sq ft.)')
plt.ylabel('price(USD)')
plt.show()


# In[94]:


x=sm.add_constant(x2)
results=sm.OLS(y1,x2).fit()
results.summary()


# In[95]:


plt.scatter(x2,y1)
y_hat=329.7765*x2
fig=plt.plot(x2,y_hat, lw=3,c='red',label='regression line')
plt.xlabel('size(Sq. ft)',fontsize=15)
plt.ylabel('price(USD)',fontsize=15)
plt.title('Regression Model of House size vs. price')
plt.plot()


# In[ ]:





# In[ ]:




