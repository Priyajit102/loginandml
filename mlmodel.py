#!/usr/bin/env python
# coding: utf-8

# # 1. Using Dummy Variables

# In[ ]:


import pandas as pd
from sklearn import linear_model 
import pickle 


# In[ ]:


df = pd.read_csv("carprices.csv")
df


# In[ ]:


dummy = pd.get_dummies(df.Car_Model)
dummy


# In[ ]:


merge = pd.concat([df,dummy],axis=1)
merge


# In[ ]:


new_df = merge.drop(['Car_Model','Mercedez Benz C class'],axis=1)
new_df


# In[ ]:


price = new_df.Sell_Price
data = new_df.drop(['Sell_Price'],axis=1)
data


# In[ ]:


reg = linear_model.LinearRegression()
reg.fit(data,price)


# In[ ]:


reg.predict(data)


pickle.dump(reg,open('mlmodel.pkl','wb'))

# 
# 
# ---
# 
# 1) Predict price of a mercedez benz that is 4 yr old with mileage 45000 using Dummy Variables.

# In[ ]:


print('$',int(reg.predict([[45000,4,0,0]])))


# 
# 
# ---
# 
# 3) Print the score (accuracy) of your model. 

# In[ ]:


print('accuracy of model is',(reg.score(data,price)*100),"%")


# #2. Using OneHotEncoding

# In[ ]:




