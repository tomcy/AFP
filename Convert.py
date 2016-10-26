#%%
import os
import glob
import pandas as pd
import statsmodels.api as sm
def UniqueHeader(lst): 
    Unique = []
    Unique.append('Zip')
    Unique.append('Year')
    for i in range(1,len(lst)):    #get varaible names not including year
        if lst[i][0:-4] != lst[i-1][0:-4]:
            Unique.append(lst[i][0:-4])  
    return Unique
    
def SigFacts(Depen,Indep):
    Indep = sm.tools.add_constant(Indep,has_constant='add')
    model = sm.OLS(Depen, Indep).fit()
    SigInd = Indep.loc[:,(model.pvalues <= .01)]
    NonInd = Indep.loc[:,(model.pvalues > .01)]
    while len(NonInd.T) >1 :
        model = sm.OLS(Depen,SigInd).fit()    
        Pvalues = model.pvalues
        NonInd = SigInd.loc[:,(Pvalues > .01)]
        SigInd = SigInd.loc[:,(Pvalues <= .01)] 
    return SigInd
path = "D:\Zip"
all_files = glob.glob(os.path.join(path,"*.csv"))
Data = pd.DataFrame()
Title = []
for f in all_files:
    Temp = pd.read_csv(f)
    Title.append(Temp.columns)
    Data = pd.concat((Data,Temp),axis = 1, ignore_index=True)
    del Temp
del f,all_files,path
Zillow = open('D:\Median\DepData.csv')
Median = pd.read_csv(Zillow)
Median = Median[Median['State']=='CA']
Median = Median.drop(Median.columns[[1]],axis=1)
Median = Median.rename(columns = {'RegionName':'Zip'})
Header = []
for x in Title:
    for i in x:
        Header.append(i)
Data.columns = Header
Zip= Data.iloc[:,0]
Data = Data.drop(Data.columns[[97]], axis=1)
Data.insert(0,'Zip',Zip)
del Zip
Data = pd.merge(Median, Data,on=['Zip'] ,how='outer')
Header = Data.columns 
Uni = UniqueHeader(Header)
Data =Data.dropna()
del Median,i
Ind10 = []
Ind11 = []
Ind12 = []
Ind13 = []
Ind14 = []
Ind15 = []
for i in range(0,len(Header)):
    if Header[i][-4:] == '2010':
        Ind10.append(i)
    elif Header[i][-4:] == '2011':
        Ind11.append(i)
    elif Header[i][-4:] == '2012':
        Ind12.append(i)
    elif Header[i][-4:] == '2013':
        Ind13.append(i)
    elif Header[i][-4:] == '2014':
        Ind14.append(i)
    elif Header[i][-4:] == '2015':
        Ind15.append(i)
matrix10 = pd.DataFrame(columns=Uni)
matrix11 = pd.DataFrame(columns=Uni)
matrix12 = pd.DataFrame(columns=Uni)
matrix13 = pd.DataFrame(columns=Uni)
matrix14 = pd.DataFrame(columns=Uni)
matrix15 = pd.DataFrame(columns=Uni)
for index, row in Data.iterrows():   
    newrow10 = pd.DataFrame(row[Ind10]).T 
    newrow11 = pd.DataFrame(row[Ind11]).T
    newrow12 = pd.DataFrame(row[Ind12]).T
    newrow13 = pd.DataFrame(row[Ind13]).T
    newrow14 = pd.DataFrame(row[Ind14]).T
    newrow15 = pd.DataFrame(row[Ind15]).T
    
    newrow10.insert(0,'Year',2010)    
    newrow10.insert(0,'Zip',row[0]) 
    newrow10.columns = Uni
    matrix10 = pd.concat([matrix10,newrow10],axis=0,ignore_index=True,copy=False)
    
    newrow11.insert(0,'Year',2011)    
    newrow11.insert(0,'Zip',row[0]) 
    newrow11.columns = Uni
    matrix11 = pd.concat([matrix11,newrow11],axis=0,ignore_index=True,copy= False)    
    
    newrow12.insert(0,'Year',2012)    
    newrow12.insert(0,'Zip',row[0]) 
    newrow12.columns = Uni
    matrix12 = pd.concat([matrix12,newrow12],axis=0,ignore_index=True,copy = False)    
    
    newrow13.insert(0,'Year',2013)    
    newrow13.insert(0,'Zip',row[0]) 
    newrow13.columns = Uni
    matrix13 = pd.concat([matrix13,newrow13],axis=0,ignore_index=True, copy = False)    

    newrow14.insert(0,'Year',2014)    
    newrow14.insert(0,'Zip',row[0]) 
    newrow14.columns = Uni
    matrix14 = pd.concat([matrix14,newrow14],axis=0,ignore_index=True,copy= False)    

    newrow15.insert(0,'Year',2015)    
    newrow15.insert(0,'Zip',row[0]) 
    newrow15.columns = Uni
    matrix15 = pd.concat([matrix15,newrow15],axis=0,ignore_index=True,copy = False)
    
    Data.drop(Data.index[[0]],inplace=True)
    del newrow10,newrow11,newrow12,newrow13,newrow14,newrow15
del Data,Ind10,Ind11,Ind12,Ind13,Ind14,Ind15,row,index,i
Final = pd.concat([matrix10,matrix11,matrix12,matrix13,matrix14,matrix15],ignore_index=True,copy=False)
del matrix10,matrix11,matrix12,matrix13,matrix14,matrix15,Uni
Final['Zip'] = Final['Zip'].astype(int)
Final['Housing, Median Year Built, '] = Final['Year'] - Final['Housing, Median Year Built, ']
Final['Housing, Median Year Moved In, '] = Final['Year'] - Final['Housing, Median Year Moved In, ']
#DO NOT TOUCH
