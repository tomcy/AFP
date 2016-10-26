
# coding: utf-8

# In[1]:

# read clean data
import pandas as pd
data = pd.read_csv("clean_data.csv")
print("Total size after cleaning ", data.shape)


# In[2]:

# show the first five rows
data.head(n=5)


# In[3]:

# seperate data into three buckets
good = ['1-30 DPD', 'Current', 'Paid', 'Matured']
inter = ['31-60 DPD', 'Insurance', '61-90 DPD', 'No Performance Data Available']
bad = ['Balance Owed', 'Assigned for Repossession', 'Recovered', '90+ DPD', 'Bankruptcy']
for item in good:
    data.loc[data.loc[:, 'PERFORMANCE'] == item, 'default'] = 0
for item in inter:
    data.loc[data.loc[:, 'PERFORMANCE'] == item, 'default'] = 1
for item in bad:
    data.loc[data.loc[:, 'PERFORMANCE'] == item, 'default'] = 2  
data = data.loc[((data.loc[:, 'default'] == 0) | (data.loc[:, 'default'] == 1)) | (data.loc[:, 'default'] == 2), :]
print("good size = ", data.loc[data.loc[:, 'default'] == 0, :].shape)
print("intermediate size = ", data.loc[data.loc[:, 'default'] == 1, :].shape)
print("bad size = ", data.loc[data.loc[:, 'default'] == 2, :].shape)


# In[9]:

# seperate for training data and testing data
train_data = data.sample(frac=0.7)
train_data.sort_values('analyticsmatchkey', inplace = True)
test_data = data[~data.index.isin(train_data.index)]
print(train_data.head(n=5))
print(test_data.head(n=5))
print("Number of training data = ", len(train_data))
print("Nuber of testing data = ", len(test_data))


# In[47]:

# prepare the data for training
# features
# time with bank (LINKA053)
features = ['LINKA053']

# extract data from training data
cleaned_data = pd.DataFrame()
for feature in features:
    cleaned_data = pd.concat([cleaned_data, train_data.loc[:, feature]], axis=1)
cleaned_data = pd.concat([cleaned_data, train_data.loc[:, 'default']], axis=1)
# clean data
cleaned_data.dropna(inplace = True)
# delete the data with 99999 value
for feature in features:
    cleaned_data = cleaned_data.loc[cleaned_data.loc[:, feature] != 99999, :]
# set X and y
y = cleaned_data.loc[:, 'default']
X = cleaned_data.iloc[:, :-1]
print(X.head())
print(y.head())


# In[48]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.scatter(X.iloc[:, 0], y)


# In[49]:

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)

