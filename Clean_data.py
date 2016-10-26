
# coding: utf-8

# In[1]:

# cleaning data
# The file included declines, walkaways, and booked accounts
# keep: Flags = funded or repayment
import pandas as pd
data = pd.read_csv(".\data\PRM.EDTOUT.DGMMOTOL.CUSTCVL2  Credit Auto.csv")
data = data.loc[(data.loc[:, 'FLAGS'] == 'funded') | (data.loc[:, 'FLAGS'] == 'repayment'), :]
data.to_csv("clean_data.csv", index=False)


# In[ ]:



