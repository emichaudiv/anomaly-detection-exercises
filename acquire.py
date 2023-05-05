#!/usr/bin/env python
# coding: utf-8

# In[1]:


txt = 'anonymized-curriculum-access.txt'


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import env


# In[3]:


#Importing all the things needed to view the data


# In[4]:


df= pd.read_table('anonymized-curriculum-access.txt',header=None)


# In[5]:


df.head()


# In[6]:


#Cheking the data 


# In[7]:


df.nunique()


# In[8]:


#Checking the amount of entries, let's clean the data


# In[9]:


df[0][0].split()


# In[10]:


#taking it appart to be aranged more coherently 


# In[11]:


parts = df[0][0].split()

output = {}
output['date'] = parts[0]
output['time'] = parts[1]
output['address'] = parts[2]
output['ip'] = parts[5]
output


# In[12]:


pd.Series(output)


# In[13]:


#It's time to make it a function


# In[14]:


def parse_log_entry(entry):
    parts = entry.split()
    output = {}

    output['date'] = parts[0]
    output['time'] = parts[1]
    output['address'] = parts[2]
    output['ip'] = parts[-1]
    return pd.Series(output)


# In[15]:


df = df[0].apply(parse_log_entry)


# In[16]:


# Now to apply to the dataframe


# In[17]:


df.head()


# In[18]:


df.ip.value_counts()


# In[19]:


#checking the count of each ip address


# In[20]:


ip_df = pd.DataFrame(df.ip.value_counts(dropna=False)).reset_index().rename(columns={'index': 'ip', 'ip': 'count'})
ip_df.head()


# In[21]:


# finding the ip with the most counts


# In[22]:


df.ip.count()


# In[23]:


#Finding the total count of all ip addresses


# In[24]:


ip_df2 = pd.DataFrame((df.ip.value_counts(dropna=False))/df.ip.count()).reset_index().rename(columns={'index': 'ip', 'ip': 'chance'})
ip_df2.head()


# In[25]:


#Checking the chances of all ip addresses 


# In[26]:


284579/900223


# In[27]:


#To see if its correct, I take the top counted ip and divide it by the total ips and compare it to the previous df


# In[28]:


ip_dfp = ip_df.merge(ip_df2, on='ip')
ip_dfp.head()


# In[29]:


#Merging the previous two df into one


# In[30]:


ip_dfp.set_index('ip')['count'].sort_values()


# In[31]:


#Setting up a way to be made into visualized graphs


# In[32]:


ip_dfp.set_index('ip')['count'].sort_values().tail(5).plot.barh()
plt.show()


# In[33]:


def ip_dfpro():
    ip_dfp.set_index('ip')['count'].sort_values().tail(5).plot.barh()
    plt.show()


# In[34]:


#A very star contrast of the first two, especially the first address.


# In[35]:


ip_dfp.set_index('ip')['count'].sort_values().tail(20).plot.barh(figsize=(5,5))
plt.show()


# In[36]:


def ip_dfp():
    ip_df.set_index('ip')['count'].sort_values().tail(20).plot.barh(figsize=(5,5))
    plt.show()


# In[37]:


#Checking to see more and it is more or less the same result.


# In[38]:


time_df = pd.DataFrame(df.time.value_counts(dropna=False)).reset_index().rename(columns={'index': 'time', 'time': 'count'})
time_df.head()


# In[39]:


#Now I decided to check the time of the access of the address


# In[40]:


time_df.tail()


# In[41]:


#Checking the tail end


# In[42]:


time_df.set_index('time')['count'].sort_values().tail(30).plot.barh()
plt.show()


# In[43]:


def time_dfp():
    time_df.set_index('time')['count'].sort_values().tail(30).plot.barh()
    plt.show()


# In[44]:


# A visualization on some of the times the ips were accessed


# In[45]:


time_df = time_df.merge(ip_df, on='count')
time_df.head(20)


# In[46]:


def df_accessp():
    time_df = time_df.merge(ip_df, on='count')
    time_df.head(20)


# In[47]:


#Combining the df togther for more detail


# In[48]:


add_df = pd.DataFrame(df.address.value_counts(dropna=False)).reset_index().rename(columns={'index': 'address', 'address': 'count'})
add_df


# In[49]:


#Now I check the address itself to see what I'm looking at


# In[50]:


add_df2 = pd.DataFrame((df.address.value_counts(dropna=False))/df.ip.count()).reset_index().rename(columns={'index': 'address', 'address': 'chance'})
add_df2.head()


# In[51]:


#Checking the likelyhood of the visits to the addresses


# In[52]:


add_dfp = add_df.merge(add_df2, on='address')
add_dfp.head()


# In[53]:


#combining the previous df together 


# In[54]:


add_dfp.set_index('address')['count'].sort_values()


# In[55]:


#checking the counts of each address


# In[56]:


add_df.set_index('address')['count'].sort_values().tail(20).plot.barh()
plt.show()


# In[57]:


def add_dfc():
    add_df.set_index('address')['count'].sort_values().tail(20).plot.barh()
    plt.show()


# In[58]:


# My findings show a '/' address being the most popular, possibly being the homepage, but it could also be a dead page


# In[59]:


add_df.set_index('address')['count'].sort_values().head(20).plot.barh()
plt.show()


# In[60]:


def add_df2c():
    add_df.set_index('address')['count'].sort_values().head(20).plot.barh()
    plt.show()


# In[61]:


#Checking the bottom of the list, mostly resources.


# In[ ]:





# In[ ]:





# In[ ]:




