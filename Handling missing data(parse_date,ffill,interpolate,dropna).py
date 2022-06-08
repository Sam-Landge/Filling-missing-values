#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Convert string column into the date type 
Use date as an index of dataframe usine set_index() method 
Use fillna() method in dataframe
Use fillna(method="ffill") method in dataframe
Use fillna(method="bfill") method in dataframe
"axis" parameter in fillna() method in dataframe
"limit" parameter in fillna() method in dataframe
interpolate() to do interpolation in dataframe
interpolate() method "time"
dropna() method Drop all the rows which has "na" in dataframe
"how" parameter in dropna() method 
"thresh" parameter in dropna() method 


# In[9]:


import pandas as pd
df=pd.read_csv('D:\weather.csv', parse_dates=['Day'])


# In[10]:


df.head()


# In[11]:


type(df.Day[0]) # First it was reading day as string. we went back in cell 9 and did parse_dates=['Day'].Now it is in time scale


# In[12]:


df.set_index('Day',inplace=True) 


# In[13]:


df # set Day as Index


# In[14]:


new_df = df.fillna(0)
new_df


# In[16]:


# It has replaced NaN by 0 but we want to in event column in place or 0 we want no event
new_df = df.fillna({'Temp': 0,'Wind Speed': 0, 'Event': 'No Event'})


# In[17]:


new_df


# In[18]:


new_df=df.fillna(method='ffill') # It is looking odd that tem is 0 so we are filling day before tem,wind speed and event by using forward fill(ffill)


# In[19]:


new_df


# In[20]:


new_df=df.fillna(method='bfill') # used back fill
new_df


# In[24]:


new_df=df.fillna(method='ffill',limit=1) # forward fill only one value


# In[25]:


new_df


# In[27]:


# we are still not happy in filling the guess so we are using the interpolate
new_df=df.interpolate()
new_df


# In[29]:


# Interpolate has filled the midle value of upper and lower number
# Still not looking right
new_df = df.interpolate(method= 'time')
new_df
# looking better


# In[30]:


new_df.dropna() # droped all having NaN values


# In[32]:


new_df.dropna(how='all') # removing the row which has all NaN values


# In[35]:


new_df.dropna(thresh=2) # if it has 2 value e.g tem,wind speed or evend keep it otherwise if less then 2 drop itdf
new_df


# In[36]:


dt=pd.date_range('01-01-2017','04-12-2017')
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)
df


# In[39]:


df=df.interpolate(method='time')
df


# In[45]:


df_cmp=df.fillna({'Event':'No Event'})


# In[50]:


df_cmp.tail(60)


# In[ ]:




