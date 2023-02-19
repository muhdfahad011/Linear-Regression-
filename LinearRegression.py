# # Linear Regression

#  linear relationship between page speed and amount purchased:

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from pylab import *

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

scatter(pageSpeeds, purchaseAmount)




# In[2]:


from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)


# 

# In[3]:


r_value ** 2


# using slope and intercept we got from the regression to plot predicted values vs. observed:

# In[4]:


import matplotlib.pyplot as plt

def predict(x):
    return slope * x + intercept

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()




# In[ ]:




