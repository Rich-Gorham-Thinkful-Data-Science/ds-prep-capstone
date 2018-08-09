import pandas as pd
import numpy as np

def resistance_level(df,usp):

    #Pull columns of interest
    sub_set_1 = df[['Data Year', 'Region Name', 'Age Group', \
                      'Specimen Source', 'Genus']]

    #Pull columns with 'Concl'
    sub_set_2 = pd.DataFrame(df.filter(regex = 'Concl'))
    sub_set_2.fillna("NA", inplace = True)

    #Concatenate two data frames
    frames_set = [sub_set_1, sub_set_2]
    data_2 = pd.concat(frames_set, axis=1)

    #Count rows for resistance
    data_2['sum_R'] = data_2.apply(lambda row: sum(row == 'R') ,axis = 1)
    data_2['sum_S'] = data_2.apply(lambda row: sum(row == 'S') ,axis = 1)
    data_2['sum_I'] = data_2.apply(lambda row: sum(row == 'I') ,axis = 1)

    #Pivot on resitance
    series_2_All = data_2.groupby(['Data Year'])\
                   ['sum_R', 'sum_S', 'sum_I'].sum()
    series_2_All['sum_All'] = series_2_All.sum(axis = 1, skipna = True)
    series_2_All.reset_index(level=0, inplace=True)
    
    #Concatenate US population
    frames_All = (series_2_All, usp)
    set_2_All = pd.concat(frames_All, axis = 1)
    
    #Scale to population
    set_2_All['sum_All_per_MMcap'] = set_2_All['sum_All'] / set_2_All['Value']
    set_2_All['sum_R_per_MMcap'] = set_2_All['sum_R'] / set_2_All['Value']
    set_2_All['sum_S_per_MMcap'] = set_2_All['sum_S'] / set_2_All['Value']
    set_2_All['sum_I_per_MMcap'] = set_2_All['sum_I'] / set_2_All['Value']

    #Mask Genera
    mask_Es = (data_2['Genus'] == 'Escherichia')
    mask_Ca = (data_2['Genus'] == 'Campylobacter')
    mask_Sa = (data_2['Genus'] == 'Salmonella')
    mask_Sh = (data_2['Genus'] == 'Shigella')

    #Assign series to applied mask
    series_2_Es = \
        data_2[mask_Es].groupby(['Data Year'])['sum_R', 'sum_S', 'sum_I'].sum()
    series_2_Ca = \
        data_2[mask_Ca].groupby(['Data Year'])['sum_R', 'sum_S', 'sum_I'].sum()
    series_2_Sa = \
        data_2[mask_Sa].groupby(['Data Year'])['sum_R', 'sum_S', 'sum_I'].sum()
    series_2_Sh = \
        data_2[mask_Sh].groupby(['Data Year'])['sum_R', 'sum_S', 'sum_I'].sum()

    #Sum all resistance values
    series_2_Es['sum_All'] = series_2_Es.sum(axis = 1)
    series_2_Ca['sum_All'] = series_2_Ca.sum(axis = 1)
    series_2_Sa['sum_All'] = series_2_Sa.sum(axis = 1)
    series_2_Sh['sum_All'] = series_2_Sh.sum(axis = 1)

    #Reset Indecies
    series_2_Es.reset_index(level = 0, inplace = True)
    series_2_Ca.reset_index(level = 0, inplace = True)
    series_2_Sa.reset_index(level = 0, inplace = True)
    series_2_Sh.reset_index(level = 0, inplace = True)

    #Add blank rows in Campylobacter and Shigella data sets
    set_0_Ca = pd.DataFrame(series_2_Ca)
    blank_row = []
    blank_row.insert(0, {'Data Year':1996, 'sum_R':0, 'sum_S':0,\
                     'sum_I':0, 'sum_NA':0, 'sum_All':0})
    set_1_Ca = \
        pd.concat([pd.DataFrame(blank_row), set_0_Ca], \
                   ignore_index = True,sort = False)
    set_1_Ca.fillna(0, inplace = True)

    set_0_Sh = pd.DataFrame(series_2_Sh)
    blank_row = []
    blank_row.insert(0,{'Data Year':1998, 'sum_R':0, 'sum_S':0,\
                        'sum_I':0, 'sum_NA':0, 'sum_All':0})
    blank_row.insert(0,{'Data Year':1997, 'sum_R':0, 'sum_S':0,\
                        'sum_I':0, 'sum_NA':0, 'sum_All':0})
    blank_row.insert(0,{'Data Year':1996, 'sum_R':0, 'sum_S':0,\
                        'sum_I':0, 'sum_NA':0, 'sum_All':0})
    set_1_Sh = \
        pd.concat([pd.DataFrame(blank_row), set_0_Sh], \
                   ignore_index = True,sort = False)
    set_1_Sh.fillna(0,inplace = True)
    
    #Concatenate to US Population
    frames_Es = (series_2_Es, usp)
    frames_Ca = (set_1_Ca, usp)
    frames_Sa = (series_2_Sa, usp)
    frames_Sh = (set_1_Sh, usp)

    set_2_Es = pd.concat(frames_Es, axis = 1)
    set_2_Ca = pd.concat(frames_Ca, axis = 1)
    set_2_Sa = pd.concat(frames_Sa, axis = 1)
    set_2_Sh = pd.concat(frames_Sh, axis = 1)
    
    #Scale data to population
    set_2_Es['sum_All_per_MMcap'] = set_2_Es['sum_All'] / set_2_Es['Value']
    set_2_Es['sum_R_per_MMcap'] = set_2_Es['sum_R'] / set_2_Es['Value']
    set_2_Es['sum_S_per_MMcap'] = set_2_Es['sum_S'] / set_2_Es['Value']
    set_2_Es['sum_I_per_MMcap'] = set_2_Es['sum_I'] / set_2_Es['Value']

    set_2_Ca['sum_All_per_MMcap'] = set_2_Ca['sum_All'] / set_2_Ca['Value']
    set_2_Ca['sum_R_per_MMcap'] = set_2_Ca['sum_R'] / set_2_Ca['Value']
    set_2_Ca['sum_S_per_MMcap'] = set_2_Ca['sum_S'] / set_2_Ca['Value']
    set_2_Ca['sum_I_per_MMcap'] = set_2_Ca['sum_I'] / set_2_Ca['Value']
    
    set_2_Sa['sum_All_per_MMcap'] = set_2_Sa['sum_All'] / set_2_Sa['Value']
    set_2_Sa['sum_R_per_MMcap'] = set_2_Sa['sum_R'] / set_2_Sa['Value']
    set_2_Sa['sum_S_per_MMcap'] = set_2_Sa['sum_S'] / set_2_Sa['Value']
    set_2_Sa['sum_I_per_MMcap'] = set_2_Sa['sum_I'] / set_2_Sa['Value']
    
    set_2_Sh['sum_All_per_MMcap'] = set_2_Sh['sum_All'] / set_2_Sh['Value']
    set_2_Sh['sum_R_per_MMcap'] = set_2_Sh['sum_R'] / set_2_Sh['Value']
    set_2_Sh['sum_S_per_MMcap'] = set_2_Sh['sum_S'] / set_2_Sh['Value']
    set_2_Sh['sum_I_per_MMcap'] = set_2_Sh['sum_I'] / set_2_Sh['Value']


   #Group by data
    series_2_All = data_2.groupby(['Region Name'])['sum_R', 'sum_I'].sum()
    series_2_All_region = \
        series_2_All.reindex(index = ['Region 1', 'Region 2','Region 3', \
                                      'Region 4', 'Region 5','Region 6',\
                                      'Region 7', 'Region 8', 'Region 9', \
                                      'Region 10'])

    series_2_All = data_2.groupby(['Age Group'])['sum_R', 'sum_I'].sum()
    series_2_All_age = \
        series_2_All.reindex(index = ['=""', '="0-4"', '="5-9"','="10-19"',\
                                      '="20-29"', '="30-39"', '="40-49"',\
                                      '="50-59"', '="60-69"', '="70-79"', \
                                      '="80+"'])

    series_2_All = \
        data_2.groupby(['Specimen Source'])['sum_R', 'sum_S', 'sum_I'].sum()
    series_2_All_source = \
        series_2_All.reindex(index = ['Abscess', 'Blood', 'CSF','Gall Bladder', \
                                      'Stool', 'Urine', 'Wound', 'Not Given', \
                                      'Other', 'Unknown'])

    return{'set_2_All':set_2_All, 'set_2_Es':set_2_Es, 'set_2_Ca':set_2_Ca,
           'set_2_Sa':set_2_Sa, 'set_2_Sh':set_2_Sh,
           'series_2_All_region':series_2_All_region,
           'series_2_All_age':series_2_All_age,
           'series_2_All_source':series_2_All_source}








    
