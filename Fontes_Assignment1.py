#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load packages
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)


# In[4]:


plt.plot(x,y,x,z)
plt.xlabel('x')
plt.ylabel('sin(x) and cos(x)')
plt.title('Python Refresher: Plot of sin(x) and cos(x)')
plt.legend(['sin(x)', 'cos(x)'])
plt.show

