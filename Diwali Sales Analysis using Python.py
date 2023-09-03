#!/usr/bin/env python
# coding: utf-8

# # Conducting Diwali Sales Analysis using Python

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# To avoid encoding error (ENC), using "unicode_escape"
df=pd.read_csv('C:\\Users\\hp\\OneDrive\Desktop\\Diwali Sales Data.csv',encoding = "unicode_escape")
df.shape


# In[4]:


df.head()


# # Preparing and cleaning the data for analysis

# In[5]:


df.info()


# In[6]:


#drop blank/unrelated columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[7]:


#Recheck the datashape after dropping blank/unrelated columns
df.info()


# In[8]:


#check for null vaues
df.isnull().sum()


# In[9]:


#drop the null values and save it into the dataframe
df.dropna(inplace=True)


# In[10]:


#Recheck the shape of dataframe
df.isnull().sum()
df.dtypes


# In[11]:


# Changing the data type of column 'Amount' from float to int
df['Amount']=df['Amount'].astype('int')


# In[12]:


#check the data type of 'Amount' column after conversion
df['Amount'].dtypes


# In[13]:


df.describe()


# In[14]:


#use describe method for specific column
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis (EDA)
Exploratory Data Analysis (EDA) involves examining and analyzing data in order to uncover initial insights, patterns, and trends.
# # Based on Gender

# Q#1:What insights can be derived from analyzing order placement data to identify potential patterns or trends in purchasing behavior across different genders?

# In[15]:


ax=sns.countplot(x='Gender',data=df)
for lbls in ax.containers:
    ax.bar_label(lbls)


# In[16]:


pur_gender=df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)
pur_gender


# In[94]:


ax = sns.barplot(x = "Gender", y = "Amount", data = pur_gender)

From the above graph, it's clear that the majority of buyers are female, and their purchasing influence outweighs that of males.
# # Based on Age

# Q#2: which age group, considering gender, demonstrates a greater frequency of orders?

# In[17]:


ax=sns.countplot(x='Age Group', data=df, hue='Gender')
for lbls in ax.containers:
    ax.bar_label(lbls)

From the above graph, it's clear that females within the 26-35 age group contributed to the volume of orders
# Q#3: which age group, demonstrates a greater frequency of purchases?

# In[18]:


pur_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
pur_age


# In[109]:


ax= sns.barplot(x='Age Group', y='Amount',data=pur_age,errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)

The above chart indicates that age group of 26-35 contributed high to the volume of purchases.
# # Based on the States

# Q#4: What is the  total number of orders originating from the highest-ranking (10) states?"
# 
# 
# 
# 
# 

# In[19]:


st=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
st


# In[20]:


sns.set(rc={'figure.figsize':(17,6)})
ax = sns.barplot(x = "State", y = "Orders", data = st)
for i in ax.containers:
    ax.bar_label(i,)


# The graph above illustrates a substantial contribution to the majority of orders from states such as Uttar Pradesh, Maharashtra, and Karnataka.

# Q#5: which state has spent more money on purchasing goods?

# In[21]:


sales_state=df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From the above graph, we noticed that most of the sales are from the Uttar Pradesh, Maharashtra, and Karnataka.

# # Based on the Marital Status

# In[22]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[24]:


marital_status = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = marital_status, x = 'Marital_Status',y= 'Amount', hue='Gender')


# we can see that, females (married) has purchasing more goods.

# # Based on the Occupation

# In[25]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


occup = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = occup, x = 'Occupation',y= 'Amount')


# Based on the visual representation provided in the graphs above, it's evident that a significant portion of the buyers is employed within the IT, Healthcare, and Aviation sectors.

# # Based on the Product

# In[27]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[28]:


prod = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = prod, x = 'Product_Category',y= 'Amount')


# it's apparent that a majority of the products sold belong to the Food, Clothing, and Electronics categories

# # Conclusion

# Women who are married and fall within the age group of 26-35 years, residing in the states of Uttar Pradesh (UP), Maharashtra, and Karnataka, and working in the IT, Healthcare, and Aviation industries, exhibit a higher inclination to purchase products within the Food, Clothing, and Electronics categories.

# In[ ]:




