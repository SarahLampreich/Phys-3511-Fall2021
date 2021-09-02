#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import math


# 
# Problem 1
# (Problem adapted from scipy.com)
# 
# Stirling's Approximation for $ln(n!)$ is:
# 
# $$
# ln(n!) \approx nln(n) − n.
# $$
# Write a program to output $ln(n!)$ and its Stirling's approximation for 2<n<20. Plot on the same graph the exact value and the approximate value as a function of n. Be sure to lable your curves and axes. Hint: the math module (and numpy.math) provides a factorial() method.

# In[6]:


X=[]
Y=[]

for x in range (3,20):
    X.append(math.log(math.factorial(x)))

for y in range (3,20):
    Y.append(y*math.log(y)-y)
    
print(X,Y)


# In[43]:


fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
n=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
plt.plot(n, X, label='$Real Value$')
plt.plot(n, Y, label='$Aprox$')
axes.legend(("Exact Value","Aprox" ))
axes.set_xlabel("n-values" )
axes.set_title("Stirling's Aproximation compared to Fuction")
axes.legend();


# ##### Problem 2, Create a numpy array of 100 7's 

# In[44]:


arr=7*np.ones(100)
arr


# Problem 3, 
# Given the numpy array below. Write a print statement that prints the array below for all values that are larger than 5.

# In[45]:


np.random.seed(0)
arr = np.random.randint(0,11,50)
print(arr)


# In[46]:


arr[arr>5]


# Problem 4
# Write a print statement that prints the below array with all values of '3' removed.

# In[47]:


np.random.seed(0)
arr2 = np.random.randint(0,6,20)
print(arr2)


# In[12]:


arr2[arr2!=3]


# Problem 5a
# Use numpy random.randn() to create a random 2D matrix array, that has 1000 entries in each dimension. When genereating the random values set the randome seed to zero.
# 
# Fixing a seed will ensure that the same random values are generated eveytime you run the cell. You can try removing the seed specification and you will notice you get different random number generations each time you run the cell. In genral it is good practice to fix the seed when debugging your code.

# In[48]:


np.random.seed(0)
np.random.rand(1000,1000)


# Problem 5b
# Create a plot that contains two subplots (one row tow pots). In each sub plot make a histogram of x and y random values from your matrix created in part a. Be sure to label your axes. The histograms will allow us to see how our data is distributed.

# In[16]:


fig, axes = plt.subplots(1,2)
np.random.seed(0)
x= np.random.randn(1000)
y=np.random.randn(1000)
fig = plt.figure()
axes[0].set_title('x')
axes[1].set_title('y')
axes[0].hist(x,bins=100)
axes[1].hist(y,bins=100)

plt.tight_layout();


# Problem 5c
# Now make a x-y scatter plot of your 2D matrix from part a. Each axis should contain one matrix dimension. Be sure to label your axes. This will allow us to see if there are any obious correlations or dependencies on one another in our data.

# In[24]:


np.random.seed(0)
x=np.random.rand(1000,1000)
y=np.random.rand(1000,1000)
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.scatter(x[0],y[1],marker='o')
ax.set_xlabel('x')
ax.set_title('Scatter')


# Problem 5d The scatter plot form part c is good for investigating dependencies, but it is often hard to judge the density of the data, i.e. how much of our data is at a particular x-y range. To see this more clearly we can make a 2D histogram plot, where color corresponding to a 2D bin changes based on the number of counts in it.
# 
# Make a 2D histogram of your 2D matrix from part a.

# In[28]:


np.random.seed(0)
x= np.random.randn(1000)
y=np.random.randn(1000)
fig= plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
#axes.set_title('x')
axes.hist2d(x,y,bins=100);


# 
# Problem 6
# Using linspace Generate 100 equally spaced points from 0 to 1. Then plot the cube of the values generated from linespace vs the linspace generated values.

# In[36]:


geegee=np.linspace(0,1,100)
G=[]
for g in geegee:
    #print(g**3)
    G.append(g**3)
plt.plot(geegee,G)
print(G)


# In[ ]:




