import pandas as pd
import numpy as np

def set_1(df, usp):
    df['indicator'] = 1 #Add indicator to count incidences
    
    series_1 = df.groupby(['Data Year', 'Genus'])['indicator'].count()
    
    set_0 = pd.DataFrame(series_1.unstack(level = -1))
    
    #replace NaN with zero so regression can be calculated
    set_0.replace(np.nan, 0, inplace=True) 
    set_0['All Enteric'] = set_0.sum(axis=1, skipna=True)
    
    #Reset index column from Data Year, to new index
    set_0.reset_index(level=0, inplace=True) 
    frames = (set_0, usp)

    #Concatenate the CDC data set to population
    set_1 = pd.concat(frames, axis=1)
    
    set_1['Campylobacter_per_MMcap'] = set_1['Campylobacter'] / set_1['Value']
    set_1['Escherichia_per_MMcap'] = set_1['Escherichia'] / set_1['Value']
    set_1['Salmonella_per_MMcap'] = set_1['Salmonella'] / set_1['Value']
    set_1['Shigella_per_MMcap'] = set_1['Shigella'] / set_1['Value']
    set_1['All_per_MMcap'] = set_1['All Enteric'] / set_1['Value']

    return set_1
