#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import pandas as pd

df=pd.read_csv("WHO COVID-19 global table data August 23rd.csv")
df


# In[ ]:


#Drop any NaN entry(missing value),in this case we drop the row with the NaN entry
df.dropna(axis=0,inplace=True)
df


# In[ ]:


#Here we set an inde
new_data = df.set_index("WHO Region")
new_data


# In[ ]:


#Here we sort the data frame in an ascending order
new_data.sort_values(by="WHO Region")


# The DataFrame.drop() used below removes the rest of the rows with no Value(Africa)

# In[ ]:


new_data.drop(['Americas','Europe','Western Pacific','South-East Asia','Eastern Mediterranean'],inplace=True)


# In[ ]:


#This is the final dataframe
new_data


# In[ ]:


new_data.reset_index()


# In[ ]:


#We set a new index column since we are concerned with countries
new_data.set_index("Name",inplace=True)


# In[ ]:


new_data


# In[ ]:




