#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df = pd.read_csv("data/raw.csv")
df.head()


# In[3]:


melted = df.melt(['Year', 'Denomination', 'Source'], ['Ministers', 'Communicant Members', 'Presbyteries', 'Congregations'], value_name="count", var_name="Type")


# In[4]:


melted.head()


# In[5]:



melted['Year'] = pd.to_datetime(melted['Year'], format="%Y")


# In[6]:


charts = []
for d in melted['Denomination'].unique():
    c = alt.Chart(melted[melted["Denomination"] == d].dropna()).mark_circle().encode(
            alt.X(
                'Year',
                title='Year',
                scale=alt.Scale(zero=False),
            ),
            alt.Y('count'),
            row=alt.Row("Type"),
            tooltip=["count", "Source"], 
        ).resolve_scale(y='independent').properties(
            title=d
        ).properties(width=600, height=100)
    charts.append(c)


# In[7]:


chart = alt.vconcat(*charts)


# In[8]:


chart


# In[9]:


chart.save("site/data/chart.json")

