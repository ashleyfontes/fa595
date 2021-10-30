#!/usr/bin/env python
# coding: utf-8

# # Part 1

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[11]:


names = []
purposes = []


# In[12]:


for i in range(1,51):
    # Get website text
    url = 'http://3.85.131.173:8000/random_company'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    
    # Store Name & Purpose 
    nameCheck = 'Name'
    name = [idx for idx in text if idx.lower().startswith(nameCheck.lower())]
    names.insert(0, name[0][6:])
    
    purposeCheck = 'Purpose'
    purpose = [idx for idx in text if idx.lower().startswith(purposeCheck.lower())]
    purposes.insert(0, purpose[0][9:])


# In[13]:


companyInfo = pd.DataFrame([names,purposes]).T
companyInfo.columns =['Name', 'Purpose']
print(companyInfo)


# In[14]:


companyInfo.to_csv('companyInfo.txt', sep='\t', index=False)


# In[ ]:





# # Part 2

# In[55]:


# Import files from group members
sherriCompanies = pd.read_csv('sherriCompanies.csv')
sherriCompanies.columns =['Name', 'Purpose']
gloriaCompanies = pd.read_csv('gloriaCompanies')
joeCompanies = pd.read_csv('names.purposes.try9.csv')
joeCompanies.columns =['Name', 'Purpose']


# In[57]:


# Combine files
companyPurpose = pd.concat([companyInfo, sherriCompanies, gloriaCompanies, joeCompanies], ignore_index = True)
companyPurpose


# In[ ]:





# # Part 3

# In[62]:


import os
import glob
import matplotlib.pyplot as plt
import io
import sys
import nltk
import nltk.corpus


# In[64]:


txt = companyPurpose.to_string()


# In[142]:


purposeString = companyPurpose['Purpose'].to_string()


# In[147]:


from textblob import TextBlob

blob = TextBlob(purposeString)
blob


# In[148]:


blobDF = blob.to_frame()


# In[ ]:





# In[ ]:


# Sources: 
# https://poopcode.com/python-code-snippet-how-to-get-text-from-a-website/ 

